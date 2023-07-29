"""empty message

Revision ID: eb15eb449500
Revises: e388bcd5e9b8
Create Date: 2023-07-29 12:48:54.051439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb15eb449500'
down_revision = 'e388bcd5e9b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('slot', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tableid', sa.Integer(), nullable=True))
        batch_op.drop_constraint('slot_bableid_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'tables', ['tableid'], ['id'])
        batch_op.drop_column('bableid')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('slot', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bableid', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('slot_bableid_fkey', 'tables', ['bableid'], ['id'])
        batch_op.drop_column('tableid')

    # ### end Alembic commands ###