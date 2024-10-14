import shutil
import argparse
from pathlib import Path


def copy_files_recursively(src_dir, dest_dir):
    """
    Рекурсивно перебирає файли в директорії src_dir і копіює їх у директорію dest_dir.
    Файли сортуються за розширенням у відповідні піддиректорії.
    """
    src_dir = Path(src_dir)
    dest_dir = Path(dest_dir)

    # Перевіряємо чи існує директорія призначення, якщо ні - створюємо
    if not dest_dir.exists():
        dest_dir.mkdir(parents=True, exist_ok=True)

    # Проходимо по всіх файлах та директоріях
    for item in src_dir.rglob('*'):
        if item.is_file():
            # Виділяємо розширення файлу
            file_extension = item.suffix[1:]  # Без крапки в розширенні

            # Якщо файл без розширення, позначаємо це
            if not file_extension:
                file_extension = "no_extension"

            # Шлях до піддиректорії за розширенням
            target_dir = dest_dir / file_extension

            # Створюємо директорію за розширенням, якщо її ще немає
            target_dir.mkdir(parents=True, exist_ok=True)

            # Копіюємо файл до піддиректорії
            try:
                shutil.copy2(item, target_dir / item.name)
                print(f"Файл {item.name} скопійований до {target_dir}")
            except Exception as e:
                print(f"Не вдалося скопіювати файл {item.name}: {e}")


def main():
    # Налаштовуємо парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання та сортування файлів за розширенням.')
    parser.add_argument('src_dir', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', nargs='?', default='dist', type=str, help='Шлях до директорії призначення (за замовчуванням dist)')
    
    args = parser.parse_args()

    # Перевіряємо, чи вихідна директорія існує
    src_path = Path(args.src_dir)
    if not src_path.exists() or not src_path.is_dir():
        print(f"Директорія {args.src_dir} не існує або не є директорією.")
        return

    # Викликаємо функцію для копіювання файлів
    copy_files_recursively(args.src_dir, args.dest_dir)


if __name__ == "__main__":
    main()
