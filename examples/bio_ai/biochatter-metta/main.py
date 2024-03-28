import os
from hyperon.ext import register_atoms
from biochatter.llm_connect import GptConversation
from biochatter.prompts import BioCypherPromptEngine


def biochatter_metta_query(user_question):
    prompt_engine = BioCypherPromptEngine(
                        model_name="gpt-3.5-turbo",
                        schema_config_or_info_path="./biocypher_config/schema_config.yaml",
                    )
    """ Gene Ontology Atomspace queries: """
    # user_question="What is the term name for the ontology term with ID 'GO:0000001'?"
    # user_question="Provide the description for the ontology term with ID 'GO:0000002'."
    # user_question="What are the synonyms for the ontology term with ID 'GO:0002088'?"
    # user_question="In which subontology does the ontology term with ID 'GO:0001654' belong?"
    # user_question="What is the source URL for the ontology term with ID 'GO:0000015'?"
    # user_question="What is the term name for the ontology term with ID 'GO:0000981'?"
    # user_question="Give the description for the ontology term with ID 'GO:0000785'."
    # user_question = "What is the subontology of the ontology term with ID 'GO:0000011'?"
    # user_question = "Provide the term name and subontology for the ontology term with ID 'GO:0000785'." # ---
    # user_question = "What is the subontology of the ontology term with ID 'GO:0000015'?"
    # user_question = "Give me the term name and subontology for the ontology term with ID 'GO:0000028'."

    # Questions from Metta-Motto
    # user_question = "What are the transcripts of gene ENSG00000237491"
    # user_question = "Get properties of gene ENSG00000279139"
    # user_question = "Find pathways that gene F13A1 is a subset of"
    # user_question = "Find parent pathways of the pathways that the gene named 'FGR' is a subset of?"
    # user_question = "Find parent pathways of the pathways that FGR  gene is a subset of"

    # user_question = "What variants have eqtl association with gene HBM"
    # user_question = "What variants have eqtl association with gene ENSG00000206177"

    metta_query = prompt_engine.generate_query(user_question)
    metta_query = f"!(match &self \n {metta_query} \n)"
    print("\nMeTTa Query:\n\n", metta_query)

    # metta = MeTTa()

    # def read_metta_file(filename):
    #     with open(filename, 'r') as file:
    #         file_content = file.read()
    #     return str(file_content)

    # metta_sample = f"""\
    # {read_metta_file('./bioatomspace_data_subset/gencode/edges.metta')}\
    # {read_metta_file('./bioatomspace_data_subset/gencode/nodes.metta')}\
    # {read_metta_file('./bioatomspace_data_subset/gaf/edges.metta')}\
    # {read_metta_file('./bioatomspace_data_subset/gtex/eqtl/edges.metta')}\
    # {read_metta_file('./bioatomspace_data_subset/ontology/edges.metta')}\
    # {read_metta_file('./bioatomspace_data_subset/ontology/nodes.metta')}\
    # {read_metta_file('./bioatomspace_data_subset/reactome/edges.metta')}\
    # {read_metta_file('./bioatomspace_data_subset/reactome/nodes.metta')}\
    # {read_metta_file('./bioatomspace_data_subset/uniprot/edges.metta')}\
    # {read_metta_file('./bioatomspace_data_subset/uniprot/nodes.metta')}\

    # {str(metta_query).strip()}
    # """


    # query_result = metta.run(metta_sample)
    # print("\nMeTTa output:\n\n", query_result)


    # conversation = GptConversation(
    #     model_name="gpt-3.5-turbo",
    #     prompts={},
    #     correct=False,
    # )

    # conversation.set_api_key(
    #     api_key=os.getenv("OPENAI_API_KEY"), user="query_interactor"
    # )

    # Natural language LLM response

    # out_msg, token_usage, correction = conversation.query(f"present the following result '{query_result}' for the following query '{user_question}' in a natural language if result is present  ")
    # print("\nLLM Response:\n\n", out_msg)

@register_atoms
def biochatter_atom():
    biochatterAtom = OperationAtom('biochatter', biochatter_metta_query)
    return {
        r"biochatter": biochatterAtom,
    }

