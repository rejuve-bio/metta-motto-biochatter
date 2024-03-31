import os
from hyperon import *
from hyperon.ext import register_atoms
from .llm_connect import GptConversation
from .prompts import BioCypherPromptEngine
import os

def biochatter_metta(metta: MeTTa, *args):

    for atom in args:
        user_question = str(atom) 

    prompt_engine = BioCypherPromptEngine(
                        model_name="gpt-3.5-turbo",
                        schema_config_or_info_path="/home/user/metta-motto/examples/bio_ai/motto/agents/biochatter/biocypher_config/schema_config.yaml",
                    )
    """ Gene Ontology Atomspace queries: """
    # print(user_question)
    # user_question = "What variants have eqtl association with gene ENSG00000206177"
    # print("inside biochatter metta")
    metta_query = prompt_engine.generate_query(user_question)
    metta_query = f"!(match &space \n {metta_query} \n)"
    # print("\nMeTTa Query:\n\n", metta_query)
    # print(type(metta_query))
    return [ValueAtom(metta_query)]

# @register_atoms
# def biochatter_atom():
#     biochatterAtom = OperationAtom('biochatter', biochatter_metta_query)
#     return {
#         r"biochatter": biochatterAtom,
#     }

