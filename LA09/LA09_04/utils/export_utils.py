def export_to_json(
    data: dict[str, any] | None, path: str = "out", name: str = "test"
) -> None:
    import json
    import os

    fullpath: str = os.path.join(os.getcwd(), "LA09", path)

    if not data:
        print("Keine Daten zum exportieren!")
        return
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)
    with open(os.path.join(fullpath, f"{name}.json"), "w", encoding="utf-8") as f:
        json.dump(obj=data, fp=f, indent=4)
    print(
        f"Data wurde erfolgreich in {fullpath} mit dem filenamen {name}.json erstellt"
    )
