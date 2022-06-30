from pathlib import Path
from fastapi import APIRouter, Header, Response

router = APIRouter(prefix="/stream", tags=["Stream"])
chunk_size = 1024 * 1024


@router.get("/{name}/")
async def get_streaming_video(name: str, range: str = Header(None)):
    start, end = range.replace("bytes=", "").split("-")
    start = int(start)
    end = int(end) if end else start + chunk_size
    video_path = Path(f"app/storage/{name}")
    with open(video_path, "rb") as video:
        video.seek(start)
        data = video.read(end - start)
        file_size = video_path.stat().st_size
        if end >= file_size:
            end = file_size - 1
        headers = {
            'Content-Range': f'bytes {start}-{end}/{file_size}',
            'Accept-Ranges': 'bytes'
        }
        return Response(data, status_code=206, headers=headers, media_type="video/mp4")
