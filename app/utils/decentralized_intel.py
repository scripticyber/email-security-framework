import ipfshttpclient

client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')  # Assume local IPFS node in Docker

def share_iocs(iocs: list) -> str:
    hashed_iocs = [hash(ioc) for ioc in iocs]  # Simplified
    cid = client.add_json({"iocs": hashed_iocs})
    return cid

def query_ipfs(cid: str) -> dict:
    return client.get_json(cid)