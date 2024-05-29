import json
import azure.functions as func
import logging

import os

from database import Database

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
        
@app.route(route="branch", methods=["GET"])
def getBrach(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        dict_data = db.get_by_db_name(Database.BRANCH)
        db.close_connection() 

        return func.HttpResponse(
            json.dumps(dict_data),
            mimetype="application/json",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

@app.route(route="branch", methods=["POST"])
def postBranch(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        req_body = req.get_json()
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        db.insert_by_db_name(Database.BRANCH, req_body)
        db.close_connection() 

        return func.HttpResponse(
            "Branch added successfully",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

@app.route(route="branch", methods=["DELETE"])
def deleteBranch(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        id = req.params.get('id')
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        db.delete_by_name_and_id(Database.BRANCH, Database.BRANCH_ID, id)
        db.close_connection() 

        return func.HttpResponse(
            "Branch deleted successfully",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

@app.route(route="employee", methods=["GET"])
def getEmployee(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        dict_data = db.get_by_db_name(Database.EMPLOYEE)
        db.close_connection() 

        return func.HttpResponse(
            json.dumps(dict_data),
            mimetype="application/json",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

@app.route(route="employee", methods=["POST"])
def postEmployee(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        req_body = req.get_json()
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        db.insert_by_db_name(Database.EMPLOYEE, req_body)
        db.close_connection() 

        return func.HttpResponse(
            "Employee added successfully",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

@app.route(route="employee", methods=["DELETE"])
def deleteEmployee(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        id = req.params.get('id')
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        db.delete_by_name_and_id(Database.EMPLOYEE, Database.EMPLOYEE_ID, id)
        db.close_connection() 

        return func.HttpResponse(
            "Employee deleted successfully",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

@app.route(route="client", methods=["GET"])
def getClient(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        dict_data = db.get_by_db_name(Database.CLIENT)
        db.close_connection() 

        return func.HttpResponse(
            json.dumps(dict_data),
            mimetype="application/json",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

@app.route(route="client", methods=["POST"])
def postClient(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        req_body = req.get_json()
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        db.insert_by_db_name(Database.CLIENT, req_body)
        db.close_connection() 

        return func.HttpResponse(
            "Client added successfully",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )
        
@app.route(route="client", methods=["DELETE"])
def deleteClient(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        id = req.params.get('id')
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        db.delete_by_name_and_id(Database.CLIENT, Database.CLIENT_ID, id)
        db.close_connection() 

        return func.HttpResponse(
            "Client deleted successfully",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

@app.route(route="works_with", methods=["GET"])
def getWorks_with(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        dict_data = db.get_by_db_name(Database.WORKS_WITH)
        db.close_connection() 

        return func.HttpResponse(
            json.dumps(dict_data),
            mimetype="application/json",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

@app.route(route="works_with", methods=["POST"])
def postWorks_with(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        req_body = req.get_json()
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        db.insert_by_db_name(Database.WORKS_WITH, req_body)
        db.close_connection() 

        return func.HttpResponse(
            "Works With added successfully",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

@app.route(route="works_with", methods=["DELETE"])
def deleteWorks_with(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        employee_id = req.params.get('employee_id')
        client_id = req.params.get('client_id')
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        db.delete_by_name_and_employee_id_and_client_id(Database.WORKS_WITH, employee_id, client_id)
        db.close_connection() 

        return func.HttpResponse(
            "Works With deleted successfully",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )
        
@app.route(route="branch_supplier", methods=["GET"])
def getBranch_supplier(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        dict_data = db.get_by_db_name(Database.BRANCH_SUPPLIER)
        db.close_connection() 

        return func.HttpResponse(
            json.dumps(dict_data),
            mimetype="application/json",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

@app.route(route="branch_supplier", methods=["POST"])
def postBranch_supplier(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        req_body = req.get_json()
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        db.insert_by_db_name(Database.BRANCH_SUPPLIER, req_body)
        db.close_connection() 

        return func.HttpResponse(
            "Branch Supplier added successfully",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )

@app.route(route="branch_supplier", methods=["DELETE"])
def deleteBranch_supplier(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        supplier_name = req.params.get('name')
        db = Database(os.getenv('CONNECTION_STRING_THE_OFFICE'))
        db.delete_by_name_and_supplier_name(Database.BRANCH_SUPPLIER, supplier_name)
        db.close_connection() 

        return func.HttpResponse(
            "Branch Supplier deleted successfully",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "Internal Server Error",
            status_code=500
        )