"""empty message

Revision ID: 3c9b78409e81
Revises: 3ac2225018d4
Create Date: 2024-04-03 04:04:05.593355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c9b78409e81'
down_revision = '3ac2225018d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('named_entity', schema=None) as batch_op:
        batch_op.alter_column('text_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('named_entity', schema=None) as batch_op:
        batch_op.alter_column('text_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
