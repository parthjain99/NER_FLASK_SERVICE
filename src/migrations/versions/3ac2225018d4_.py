"""empty message

Revision ID: 3ac2225018d4
Revises: 4b04ff43f67a
Create Date: 2024-04-03 03:39:31.573396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ac2225018d4'
down_revision = '4b04ff43f67a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('text_data', schema=None) as batch_op:
        batch_op.alter_column('text_id',
               existing_type=sa.INTEGER(),
               type_=sa.Text(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('text_data', schema=None) as batch_op:
        batch_op.alter_column('text_id',
               existing_type=sa.Text(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
