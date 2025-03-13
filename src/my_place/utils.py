from pathlib import Path

def get_asset_path(asset_local_path: str) -> Path:
    asset_root_dir = Path(__file__).parent.parent.parent / "assets"
    asset_path = asset_root_dir / asset_local_path
    if not asset_path.exists():
        raise FileNotFoundError(f"Asset '{asset_local_path}' not found in {asset_root_dir}")
    
    return asset_path