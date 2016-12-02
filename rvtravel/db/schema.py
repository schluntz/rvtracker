"""
Pseudo-Schema

Assumes single threaded opperation

Table status
    ts TIME UNIQUE
    status INT (0 shut down, 1 running, 2 maintanance)
Table location
    ts as TIME UNIQUE
    lat as TEXT
    long as TEXT
Table device
    id INTEGER UNIQUE
    name TEXT
    type TEXT (apm, volt, both)
Table power
    id INTEGER UNIQUE
    device INTEGER
    ts TIME
    amp FLOAT
    volt FLOAT
Table env
    ts as TIME UNIQUE
    
"""

# ['CREATE TABLE IF NOT EXISTS Messages 
    
# SQLite 3
schema{'sqlite3': \ 
          {'status': \
              '(id INTEGER UNIQUE, email TEXT, sent_at TEXT)',
          },
          {'location': \
              '(id INTEGER UNIQUE, email TEXT, sent_at TEXT)',
          },
          {'device': \
              '(id INTEGER UNIQUE, email TEXT, sent_at TEXT)',
          },
          {'device': \
              '(id INTEGER UNIQUE, email TEXT, sent_at TEXT)',
          },
          {'power': \
              '(id INTEGER UNIQUE, email TEXT, sent_at TEXT)',
          },
          {'env': \
              '(id INTEGER UNIQUE, email TEXT, sent_at TEXT)',
          }
      }
        
