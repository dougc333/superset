# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""add_save_form_column_to_db_model

Revision ID: 453530256cea
Revises: f1410ed7ec95
Create Date: 2021-04-30 10:55:07.009994

"""

# revision identifiers, used by Alembic.
revision = "453530256cea"
down_revision = "f1410ed7ec95"

import sqlalchemy as sa  # noqa: E402
from alembic import op  # noqa: E402


def upgrade():
    with op.batch_alter_table("dbs") as batch_op:
        batch_op.add_column(
            sa.Column(
                "configuration_method",
                sa.VARCHAR(255),
                server_default="sqlalchemy_form",
            )
        )


def downgrade():
    with op.batch_alter_table("dbs") as batch_op:
        batch_op.drop_column("configuration_method")
