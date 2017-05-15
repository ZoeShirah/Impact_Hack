from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """Constituent information."""

    __tablename__ = "constituent"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(75), nullable=False)
    last_name = db.Column(db.String(75), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    registration_num = db.Column(db.Float, nullable=True)

    def __repr__(self):

        return "<Name=%s zipcode=%s>" % (self.first_name,
                                         self.zipcode)


class Representative(db.Model):
    """Representative information."""

    __tablename__ = "representative"

    rep_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(75), nullable=False)
    last_name = db.Column(db.String(75), nullable=False)
    party = db.Column(db.String(75), nullable=False)
    state = db.Column(db.String(5), nullable=True)
    type_rep = db.Column(db.String(50), nullable=True)
    district = db.Column(db.String(50), nullable=True)

    def __repr__(self):

        return "<Name=%s Party=%s>" % (self.first_name,
                                       self.party)

class District(db.Model):

    __tablename__="district"

    dis_id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    district = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(5), nullable=True)

    def __repr__(self):

        return "<dis_id=%s district=%s>" % (self.dis_id,
                                       self.district)

class ZipCode(db.Model):

    __tablename__ = "zipcodes"

    zip_code = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.Integer, db.ForeignKey('district.dis_id'))

    def __repr__(self):

        return "<Zip=%d District=%s>" % (self.zip_code,
                                       self.district)


##############################################################################
# Helper functions


def connect_to_db(app, db_uri="postgresql:///voter_data"):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
    db.create_all()