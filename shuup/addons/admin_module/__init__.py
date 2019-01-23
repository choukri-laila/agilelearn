# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

from shuup.admin.base import AdminModule, MenuEntry
from shuup.admin.menu import ADDONS_MENU_CATEGORY
from shuup.admin.utils.permissions import AdminCustomModelPermissionDef
from shuup.admin.utils.urls import admin_url
from shuup.core.models import Shop


class AddonModule(AdminModule):
    name = _("Addons")
    breadcrumbs_menu_entry = MenuEntry(text=name, url="shuup_admin:addon.list")

    def get_urls(self):
        return [
            admin_url(
                "^addons/$",
                "shuup.addons.admin_module.views.AddonListView",
                name="addon.list",
                permissions=[AdminCustomModelPermissionDef(Shop, "list_addons", _("Can list addons"))]
            ),
            admin_url(
                "^addons/add/$",
                "shuup.addons.admin_module.views.AddonUploadView",
                name="addon.upload",
                permissions=[AdminCustomModelPermissionDef(Shop, "addon_upload", _("Can upload addons"))]
            ),
            admin_url(
                "^addons/add/confirm/$",
                "shuup.addons.admin_module.views.AddonUploadConfirmView",
                name="addon.upload_confirm",
                permissions=[AdminCustomModelPermissionDef(Shop, "addon_upload", _("Can upload addons"))]
            ),
            admin_url(
                "^addons/reload/$",
                "shuup.addons.admin_module.views.ReloadView",
                name="addon.reload",
                permissions=[AdminCustomModelPermissionDef(Shop, "addon_reload_app", _("Can reload application"))]
            ),
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Addons"),
                icon="fa fa-puzzle-piece",
                url="shuup_admin:addon.list",
                category=ADDONS_MENU_CATEGORY
            )
        ]
