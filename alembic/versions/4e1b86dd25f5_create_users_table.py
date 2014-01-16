"""create users table

Revision ID: 4e1b86dd25f5
Revises: None
Create Date: 2014-01-15 06:49:52.982207

"""

# revision identifiers, used by Alembic.
revision = '4e1b86dd25f5'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nickname', sa.String(64), index = True, unique = True),
        sa.Column('email', sa.String(120), index = True, unique = True),
        sa.Column('role', sa.SmallInteger, default = 0),
    )


def downgrade():
    os.drop_table('user')
