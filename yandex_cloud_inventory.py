#!/usr/bin/env python3
import json
import subprocess

def get_yandex_cloud_instances():
    try:
        # Получение данных о виртуальных машинах из Yandex Cloud CLI
        result = subprocess.run(
            ["yc", "compute", "instances", "list", "--format", "json"],
            capture_output=True,
            text=True,
            check=True
        )
        instances = json.loads(result.stdout)
        inventory = {"all": {"hosts": []}}

        # Парсинг данных о машинах
        for instance in instances:
            # Получаем внешний IP через NAT
            external_ip = instance.get("network_interfaces", [{}])[0].get("primary_v4_address", {}).get("one_to_one_nat", {}).get("address")

            if external_ip:
                inventory["all"]["hosts"].append(external_ip)

        return inventory

    except Exception as e:
        print(f"Error fetching instances: {e}")
        return {"_meta": {"hostvars": {}}}

if __name__ == "__main__":
    inventory = get_yandex_cloud_instances()
    print(json.dumps(inventory, indent=2))
