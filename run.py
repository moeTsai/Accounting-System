from order import app, db



def database_existance_check():
    """Check if database exists. If not, create it."""
    # from app import app, db
    import os
    
    if not os.path.exists('./instance/bill.db'):
        print('Database does not exist. Creating database...')
        app.app_context().push()
        db.create_all()
    else:
        print('Database exists.')




if __name__ == '__main__':
    
    database_existance_check()

    app.run(debug=True)
