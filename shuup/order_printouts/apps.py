# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from django.utils.translation import gettext_lazy as _

import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = "shuup.order_printouts"
    verbose_name = _("Order printouts")
    label = "shuup_order_printouts"

    provides = {
        "admin_module": ["shuup.order_printouts.admin_module:PrintoutsAdminModule"],
        "admin_order_section": ["shuup.order_printouts.admin_module.section:PrintoutsSection"],
    }
