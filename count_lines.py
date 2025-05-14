#!/usr/bin/env python3
import os
from pathlib import Path

# Директории, которые нужно пропускать целиком
EXCLUDE_DIRS = {
    'venv', '__pycache__', 'migrations', 'node_modules'
}

# Какие расширения файлов считаем «ручным» кодом
INCLUDE_EXTS = {'.py', '.html', '.css', '.js'}

def is_excluded(path: Path) -> bool:
    """Провека, что ни одна часть пути не входит в EXCLUDE_DIRS."""
    return any(part in EXCLUDE_DIRS for part in path.parts)

def count_lines(root: Path) -> dict:
    """
    Возвращает словарь вида:
      {
        'total': X,    # сумма по всем файлам
        '.py': Y,      # непустые строки в .py
        '.html': Z,    # в .html
        ...
      }
    """
    stats = {'total': 0}
    for ext in INCLUDE_EXTS:
        stats[ext] = 0

    for dirpath, dirnames, filenames in os.walk(root):
        # Фильтруем дочерние директории
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]

        for fname in filenames:
            fpath = Path(dirpath) / fname

            if is_excluded(fpath):
                continue

            ext = fpath.suffix.lower()
            if ext not in INCLUDE_EXTS:
                continue

            try:
                with fpath.open(encoding='utf-8') as f:
                    lines = f.readlines()
            except Exception:
                # если файл читать не удалось — пропускаем
                continue

            # Считаем только непустые (strip() != '')
            cnt = len(lines)
            stats['total'] += cnt
            stats[ext] += cnt

    return stats

if __name__ == '__main__':
    root = Path(__file__).parent.resolve()
    stats = count_lines(root)

    print("Статистика непустых строк кода:")
    print(f"  Всего: {stats['total']}")
    for ext, cnt in stats.items():
        if ext == 'total':
            continue
        print(f"  {ext:6}: {cnt}")
