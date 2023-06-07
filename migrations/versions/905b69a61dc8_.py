"""empty message

Revision ID: 905b69a61dc8
Revises: eed1484071f0
Create Date: 2023-06-07 03:16:55.830496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '905b69a61dc8'
down_revision = 'eed1484071f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bool', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cate', sa.Text(), server_default='1', nullable=True))

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_column('cate')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cate', sa.TEXT(), server_default=sa.text("'1'"), nullable=False))

    with op.batch_alter_table('bool', schema=None) as batch_op:
        batch_op.drop_column('cate')

    # ### end Alembic commands ###