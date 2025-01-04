# seeds/__init__.py

from .users_seed import seed_users  # Tüm seeder fonksiyonlarını buraya ekleyin
from .addresses_seed import seed_addresses

# Seeder fonksiyonlarını dışa aktarıyoruz
__all__ = ["seed_users", "seed_addresses"]
