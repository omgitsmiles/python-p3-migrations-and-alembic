"""Added Student Model

Revision ID: 925307dc2ddb
Revises: c87f14c0b08e
Create Date: 2023-08-01 15:58:34.121272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '925307dc2ddb'
down_revision = 'c87f14c0b08e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('enrolled_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    # ### end Alembic commands ###