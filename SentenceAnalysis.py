import json

from glob import glob
from tqdm import tqdm
from indra.statements import stmts_from_json, Statement
from pprint import pprint

index=0
files = glob("UN_stmt_jsons/*")
L = [] #Initialize an empty list L
for J in tqdm(files): #For each JSON file J in UN_stmt_jsons
    print(index)
    index+=1
    with open(J, "r") as J:
        sts = stmts_from_json(json.load(J)["statements"])
        for S in sts:  #For each INDRA statement S in J:
            #print(S.subj.db_refs.get('UN')[0][0])
            if S.subj.db_refs.get("UN") is not None and S.obj.db_refs.get("UN") is not None:
                subject = S.subj.db_refs.get('UN')[0][0].split("/")[-1]
                object = S.obj.db_refs.get('UN')[0][0].split("/")[-1]
            # If the top UN grounding for the subj is precipitation, and the top grounding for the obj is food_production:
            # .text
            #if subject=='precipitation' and object=='food_production':
                #L.append(S.evidence[0].text)

            # Get the evidence sentences from S that were read by the EIDOS machine reader.
            # (See https://indra.readthedocs.io/en/latest/modules/statements.html#indra.statements.Statement for API documentation for INDRA statements),
            # and add them to the list L.
for x in range(len(L)):
    print(L[x])


