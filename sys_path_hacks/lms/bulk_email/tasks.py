from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'bulk_email.tasks')

from lms.djangoapps.bulk_email.tasks import *
