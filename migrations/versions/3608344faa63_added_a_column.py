"""Added a column.

Revision ID: 3608344faa63
Revises: 6f0df144a032
Create Date: 2023-05-03 10:33:45.088847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3608344faa63'
down_revision = '6f0df144a032'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('author', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'author')
    # ### end Alembic commands ###
