from loader import dp
from .admin_filters import AdminFilter, AdminBotFilter
from .group_filters import IsGroup
from .private_chat_filters import IsPrivate


# if __name__ == "filters":
#     dp.filters_factory.bind(AdminFilter)
#     dp.filters_factory.bind(AdminBotFilter)
#     dp.filters_factory.bind(IsGroup)
#     dp.filters_factory.bind(IsPrivate)
