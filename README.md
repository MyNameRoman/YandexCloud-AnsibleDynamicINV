# YandexCloud-AnsibleDynamicINV
```markdown
# Dynamic Inventory for Yandex Cloud

Этот скрипт генерирует динамический инвентарь для Ansible, используя данные о виртуальных машинах из Yandex Cloud.

## Особенности
- Автоматически парсит внешние IPv4-адреса машин через NAT.
- Возвращает инвентарь в формате JSON, совместимом с Ansible.
- Поддерживает фильтрацию только машин с публичными IP.

## Требования
- Установленный и настроенный [Yandex Cloud CLI (yc)](https://cloud.yandex.ru/docs/cli/operations/install-cli)
- Python 3.6+
- Права доступа к Yandex Cloud для выполнения команды `yc compute instances list`

## Установка
1. Склонируйте репозиторий:
```bash
git clone (https://github.com/MyNameRoman/YandexCloud-AnsibleDynamicINV)
cd YandexCloud-AnsibleDynamicINV
```

2. Убедитесь, что Yandex Cloud CLI аутентифицирован:
```bash
yc init
```

3. Сделайте скрипт исполняемым:
```bash
chmod +x yc_inventory.py
```

## Использование
### 1. Прямой вызов
```bash
./yc_inventory.py
```

Пример вывода:
```json
{
  "all": {
    "hosts": [
      "84.252.142.56",
      "87.250.247.222"
    ]
  }
}
```

### 2. С Ansible
Используйте скрипт как динамический инвентарь:
```bash
ansible all -i yc_inventory.py -m ping
```

### 3. Проверка конкретной машины
```bash
ansible -i yc_inventory.py 84.252.142.56 -m ping
```

## Конфигурация
Скрипт использует стандартные настройки Yandex Cloud CLI. Убедитесь, что:
- Вы выбрали нужный облачный каталог через `yc config set folder-id <folder-id>`
- У вас есть права на выполнение `yc compute instances list`

## Ограничения
- Возвращает только машины с публичными IP через NAT
- Не учитывает внутренние IP-адреса
- Не поддерживает группировку по тегам

## Лицензия
[MIT License](LICENSE)
