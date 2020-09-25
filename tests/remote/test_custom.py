from urllib.parse import quote_plus
import pdb
import requests
from pdb import set_trace as bp

from tests.remote.common import ENTITY_BASE, authorize_headers, BRICK, QUERY_BASE

from tests.remote.data import znt_id


def test_load_ttl():
    with open('examples/data/custom_brick_v103_sample_graph.ttl', 'rb') as fp:
        headers = authorize_headers({
            'Content-Type': 'text/turtle',
        })
        resp = requests.post(ENTITY_BASE + '/upload', headers=headers, data=fp, allow_redirects=False)
        assert resp.status_code == 200

        qstr = """
            select ?s where {
              ?s a brick:Supply_Air_Temperature_Sensor
            }
        """

    headers = authorize_headers({
        'Content-Type': 'sparql-query'
    })
    resp2 = requests.post(QUERY_BASE + '/sparql', data=qstr, headers=headers)

    # Appears my graph doesn't have this proper subClassOf embedded...
    # qstr3 = """
    # select ?child ?parent where {
    #     {?parent brick:hasPart ?child .}
    #     UNION
    #     {?child brick:isPartOf ?parent .}
    #     UNION
    #     {?parent brick:feeds ?child .}
    #     UNION
    #     {?child brick:isFedBy ?parent .}
    #     ?parent a/rdfs:subClassOf* brick:Equipment .
    #     ?child a/rdfs:subClassOf* brick:Equipment .
    # }
    # """

    qstr3 = """
    select ?child ?parent where {
        {?parent brick:hasPart ?child .}
        UNION
        {?child brick:isPartOf ?parent .}
        UNION
        {?parent brick:feeds ?child .}
        UNION
        {?child brick:isFedBy ?parent .}
    }
    """

    headers = authorize_headers({
        'Content-Type': 'sparql-query'
    })
    resp3 = requests.post(QUERY_BASE + '/sparql', data=qstr3, headers=headers)
    import pdb; pdb.set_trace()

