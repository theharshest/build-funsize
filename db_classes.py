from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

status_code = {'COMPLETED': 0,         # Where should this dict reallly go to make it easily importable
                'ABORTED': 1,
                'IN_PROGRESS': 2,
                'INVALID': 3, # Do we need this?
                }
COMPLETED=1

class Partial(Base):
    """
    Defines the table called 'partial' in the database.
    Partial(int:id, str(65):identifier, int:status, char(1024):url, char(1024):location)

    PTQs (pertinent Question):
    
    - Should URLs be generated by a separate function? (Maybe.)
    - Should there be a 1to1 mapping b/w URLs and identifiers? Yes.
    - Should we remove the url  field in the light of the above? Probably?


    :id:         Inbuilt ID, auto incremented.
                 Auto incremented. (is it?)

    :identifier: The actual string (hash combination for now) used to identify
                 the partial mar.
                 The SQL 'UNIQUE' constraint is enforced on this column.
                 Can not be empty.

    :status:     Integer field used to keep track of status, see .status_code
                 for mapping from integers to meaningful statuses.
                 Can not be empty.

    :url:        The url at which the resource will be served.
                 The SQL 'UNIQUE' constraint is enforced on this column.
                 Can not be empty.

    :location:   The location/resourcename at which to access the partial
                 internally.

    """
    __tablename__='partial'

    status_code = {'COMPLETED': 0,         # Where should this dict reallly go to make it easily importable
                    'ABORTED': 1,
                    'IN_PROGRESS': 2,
                    'INVALID': 3,
                    }

    # Define Columns
    id = Column(Integer, primary_key=True)
    identifier = Column(String(65), nullable=False, unique=True) # md5_of_c1-md5_of_c2
    status = Column(Integer, nullable=False) # is it okay to use enum like stuff?
    url = Column(String(1024), nullable=False, unique=True) # Is 1024 enough?
    location = Column(String(1024))

engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(engine)
