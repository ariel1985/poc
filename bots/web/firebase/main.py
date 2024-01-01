import google.cloud.firestore as firestore
from google.cloud.firestore import Client

# Initialize Firestore DB
db = firestore.Client()

def delete_collection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).stream()
    deleted = 0

    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.to_dict()}')
        doc.reference.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)


def list_all_collections(client):
    collections = client.collections()
    for collection in collections:
        print('Collection ID: {}'.format(collection.id))

# Call the function to delete the collection
# delete_collection(db.collection('<your-collection-name>'), 100)

list_all_collections(db)

