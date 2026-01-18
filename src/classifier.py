from pathlib import Path
from enum import Enum

class FileCategory(str, Enum):
    IMAGES = "Images"
    DOCUMENTS = "Documents"
    AUDIO = "Audio"
    VIDEO = "Video"
    ARCHIVES = "Archives"
    CODE = "Code"
    EXECUTABLES = "Executables"
    OTHERS = "Others"

EXTENSION_MAP = {
    # Images
    '.jpg': FileCategory.IMAGES, '.jpeg': FileCategory.IMAGES, '.png': FileCategory.IMAGES,
    '.gif': FileCategory.IMAGES, '.bmp': FileCategory.IMAGES, '.svg': FileCategory.IMAGES,
    '.webp': FileCategory.IMAGES, '.tiff': FileCategory.IMAGES, '.ico': FileCategory.IMAGES,
    
    # Documents
    '.pdf': FileCategory.DOCUMENTS, '.doc': FileCategory.DOCUMENTS, '.docx': FileCategory.DOCUMENTS,
    '.txt': FileCategory.DOCUMENTS, '.rtf': FileCategory.DOCUMENTS, '.odt': FileCategory.DOCUMENTS,
    '.xls': FileCategory.DOCUMENTS, '.xlsx': FileCategory.DOCUMENTS, '.ppt': FileCategory.DOCUMENTS,
    '.pptx': FileCategory.DOCUMENTS, '.csv': FileCategory.DOCUMENTS, '.md': FileCategory.DOCUMENTS,
    
    # Audio
    '.mp3': FileCategory.AUDIO, '.wav': FileCategory.AUDIO, '.aac': FileCategory.AUDIO,
    '.flac': FileCategory.AUDIO, '.ogg': FileCategory.AUDIO, '.m4a': FileCategory.AUDIO,
    
    # Video
    '.mp4': FileCategory.VIDEO, '.avi': FileCategory.VIDEO, '.mkv': FileCategory.VIDEO,
    '.mov': FileCategory.VIDEO, '.wmv': FileCategory.VIDEO, '.flv': FileCategory.VIDEO,
    
    # Archives
    '.zip': FileCategory.ARCHIVES, '.rar': FileCategory.ARCHIVES, '.7z': FileCategory.ARCHIVES,
    '.tar': FileCategory.ARCHIVES, '.gz': FileCategory.ARCHIVES, '.bz2': FileCategory.ARCHIVES,
    
    # Code
    '.py': FileCategory.CODE, '.js': FileCategory.CODE, '.html': FileCategory.CODE,
    '.css': FileCategory.CODE, '.java': FileCategory.CODE, '.cpp': FileCategory.CODE,
    '.c': FileCategory.CODE, '.h': FileCategory.CODE, '.php': FileCategory.CODE,
    '.ts': FileCategory.CODE, '.go': FileCategory.CODE, '.rs': FileCategory.CODE,
    '.json': FileCategory.CODE, '.xml': FileCategory.CODE, '.sql': FileCategory.CODE,
    
    # Executables
    '.exe': FileCategory.EXECUTABLES, '.msi': FileCategory.EXECUTABLES, '.bat': FileCategory.EXECUTABLES,
    '.sh': FileCategory.EXECUTABLES, '.app': FileCategory.EXECUTABLES,
}

def classify_file(file_path: Path) -> str:
    """
    Classifies a file based on its extension.
    """
    if file_path.is_dir():
        return None
        
    ext = file_path.suffix.lower()
    return EXTENSION_MAP.get(ext, FileCategory.OTHERS).value
