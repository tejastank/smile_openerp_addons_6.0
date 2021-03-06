# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 OpenERP s.a. (<http://openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Smile Server Monitoring',
    'version': '0.1',
    'category': 'Tools',
    'description': """Smile Server Monitoring

TO USE

This module adds the following web page "/openerp/status" that displays:
    * OpenERP Server: OK + Databases list
or
    * OpenERP Server: KO + Exception (indicates if is an OpenERP or Postgresql server connection issue)

TO INSTALL

After installing it via the web client as a server addon,
add "active: True" in the file __openerp__.py of the new web addon

Suggestions & Feedback to: corentin.pouhet-brunerie@smile.fr, kevin.deldycke@smile.fr
""",
    'author': 'Smile',
    'website': 'http://www.smile.fr',
    'depends': ['base'],
    'init_xml': [],
    'update_xml': [],
    'installable': True,
    'active': False,
    'web': True,
}
