import boto3

def lambda_handler(event: any , context:any):
    user = event["user"]
    visit_count : int = 0

    #Create a DynamoDB client 
    dynamodb = boto3.resource("dynamodb")
    table_name = "visit-count-table"
    table = dynamodb.Table(table_name)
    
    #Get the current visit count
    response = table.get_item(Key={"user" : user})
    """"
    if "Item" in response:
        visit_count = response["Item"]["count"]
    
    #Increment the number of visits
    visit_count += 1

    #Put the new visit count into the table 
    table.put_item(Item={"user":user , "count":visit_count})
    """
    message = f"Hello {user}! You have visited this page {visit_count} times."
    return {"message": message}

if __name__ == "__main__":
    event = {"user":"rayfromca"}
    print(lambda_handler(event,None))