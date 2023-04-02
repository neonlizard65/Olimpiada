"""empty message

Revision ID: 05157e24d59d
Revises: 
Create Date: 2023-04-02 22:05:36.901377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05157e24d59d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subdivision',
    sa.Column('subdivisionID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('subdivisionID')
    )
    op.create_table('visitor',
    sa.Column('visitorID', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('surname', sa.String(length=50), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('patronym', sa.String(length=50), nullable=True),
    sa.Column('birthdate', sa.DateTime(), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('organization', sa.String(length=50), nullable=True),
    sa.Column('passport_series', sa.String(), nullable=True),
    sa.Column('passport_number', sa.String(), nullable=True),
    sa.Column('passport_scan', sa.String(length=255), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('visitorID')
    )
    op.create_table('employee',
    sa.Column('employeeID', sa.Integer(), nullable=False),
    sa.Column('fio', sa.String(length=50), nullable=False),
    sa.Column('subdivisionId', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=30), nullable=True),
    sa.Column('password', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['subdivisionId'], ['subdivision.subdivisionID'], ),
    sa.PrimaryKeyConstraint('employeeID')
    )
    op.create_table('request',
    sa.Column('requestID', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('type', sa.Boolean(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('reason', sa.String(), nullable=True),
    sa.Column('subdivisionId', sa.Integer(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('employeeId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employeeId'], ['employee.employeeID'], ),
    sa.ForeignKeyConstraint(['subdivisionId'], ['subdivision.subdivisionID'], ),
    sa.PrimaryKeyConstraint('requestID')
    )
    op.create_table('visit',
    sa.Column('visitID', sa.Integer(), nullable=False),
    sa.Column('employeeId', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['employeeId'], ['employee.employeeID'], ),
    sa.PrimaryKeyConstraint('visitID')
    )
    op.create_table('visitor_pass',
    sa.Column('visitor_passID', sa.Integer(), nullable=False),
    sa.Column('visitorId', sa.Integer(), nullable=True),
    sa.Column('visitId', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('reason', sa.String(), nullable=True),
    sa.Column('group', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['visitId'], ['visit.visitID'], ),
    sa.ForeignKeyConstraint(['visitorId'], ['visitor.visitorID'], ),
    sa.PrimaryKeyConstraint('visitor_passID')
    )
    op.create_table('visitor_request',
    sa.Column('visitor_requestID', sa.Integer(), nullable=False),
    sa.Column('visitorId', sa.Integer(), nullable=True),
    sa.Column('requestId', sa.Integer(), nullable=True),
    sa.Column('group', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['requestId'], ['request.requestID'], ),
    sa.ForeignKeyConstraint(['visitorId'], ['visitor.visitorID'], ),
    sa.PrimaryKeyConstraint('visitor_requestID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visitor_request')
    op.drop_table('visitor_pass')
    op.drop_table('visit')
    op.drop_table('request')
    op.drop_table('employee')
    op.drop_table('visitor')
    op.drop_table('subdivision')
    # ### end Alembic commands ###
