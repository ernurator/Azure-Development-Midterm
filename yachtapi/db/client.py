from azure.cosmos import CosmosClient, PartitionKey
import config


client = CosmosClient(config.COSMOS_DB_ENDPOINT, config.COSMOS_DB_PRIMARY_KEY)

DATABASE_NAME = 'YachtsDatabase'
database = client.create_database_if_not_exists(id=DATABASE_NAME)

CONTAINER_NAME = 'YachtsContainer'
container = database.create_container_if_not_exists(
    id=CONTAINER_NAME,
    partition_key=PartitionKey(path="/name"),
    offer_throughput=400
)


def get_yachts():
    query = 'SELECT * FROM c'

    items = list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))

    return items


def create_yacht(body):
    container.create_item(body=body)


def get_yacht(item_id, name):
    item_response = container.read_item(item=item_id, partition_key=name)
    return item_response
