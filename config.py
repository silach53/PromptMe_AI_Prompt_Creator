class Config:
    SECRET_KEY = 'my-secret-key'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///mydatabase.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    USERNAME = "workalexandr"  # замените на свой логин
    connection_string = f"postgresql+psycopg2://{USERNAME}:@localhost:5433/{USERNAME}"
    SQLALCHEMY_DATABASE_URI = connection_string
    #engine = create_engine(connection_string)
    #Session = sessionmaker(engine)
    # Replace with your database connection details
    #Base.metadata.create_all(engine)