
# 과제 
# 단일/다중 파일 업로드
# 파일 목록 조회 : 페이징, 필터링 지원
# 파일 다운로드 : 단일/다중 ZIP 다운로드
# 파일 삭제 : 단일/다중 삭제

from fastapi import FastAPI, HTTPException,UploadFile, File, Query
from fastapi.responses import FileResponse
from typing import List, Optional
import os
import zipfile
import tempfile

#태그 메타데이터
tags_metadata = [
        {
        "name": "파일 업로드",
        "description": "파일 업로드 기능"
    },
    {
        "name": "파일 다운로드",
        "description": "파일 다운로드 기능"
    },
    {
        "name": "파일 목록 조회",
        "description": "파일 목록 조회 기능"
    },
    {
        "name": "파일 삭제",
        "description": "파일 삭제 기능"
    }
]


app = FastAPI(
    title="파일 관리 시스템",
    description="파일 업로드, 다운로드, 파일목록 조회, 삭제 기능 제공",
    version="1.0.0",
    openapi_tags=tags_metadata
)

#파일 업로드
@app.post("/upload-files/",
          tags=["파일 업로드"],
          description="파일크기 제한 10MB, 확장자 제한: jpeg, png, txt, pdf, doc, docx, xls, xlsx, zip")
async def upload_files(files: list[UploadFile] = File(...)):
    
    #업로드 가능 파일 확장자 제한
    allowed_types = ["image/jpeg", "image/png", "text/plain", "application/pdf", "application/msword", 
                     "application/ms-excel", "application/zip", "application/x-zip-compressed"]
    
    #업로드 폴더 생성
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_list = []
    
    #업로드 파일 처리
    for f in files:
        if f.content_type not in allowed_types:
            raise HTTPException(
                status_code=400,
                detail=f"{f.filename}는 지원되지 않는 파일 형식입니다."
            )

        #파일 크기 체크
        content = await f.read()
        file_size = len(content)
        if file_size == 0:
            raise HTTPException(
                status_code=400,
                detail="빈 파일은 업로드할 수 없습니다."
            )
        
        if file_size > 10 * 1024 * 1024:
            raise HTTPException(
                status_code=400,
                detail="파일 크기는 10MB를 초과할 수 없습니다."
            )
        
        #파일 저장
        file_path = os.path.join(upload_dir, f.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(content)

        #파일 정보 저장
        file_list.append({
            "filename": f.filename,
            "content_type": f.content_type,
            "file_size": file_size
        })

    # 업로드 성공 메시지 반환
    return {
        "message": "파일 업로드 성공",
        "file_list": file_list
    }

#파일 다운로드
@app.get("/download-files",
         tags=["파일 다운로드"],
         description="단일/다중 파일 다운로드(zip 파일 생성)")
async def download_files(filenames: list[str] = Query(...)):
    file_paths = []
    for filename in filenames:
        file_path = os.path.join("uploads", filename)
        if not os.path.exists(file_path):
            raise HTTPException(
                status_code=404,
                detail=f"파일 {filename}을 찾을 수 없습니다."
            )
        file_paths.append(file_path)
    #단일 파일 다운로드
    if len(file_paths) == 1:
        return FileResponse(
            path = file_paths[0],
            filename = file_paths[0],
            media_type = "application/octet-stream"
        )
    #다중 파일 다운로드
    with tempfile.NamedTemporaryFile(delete=False) as temp_zip:
        with zipfile.ZipFile(temp_zip.name, "w") as zip:
            for file_path in file_paths:
                zip.write(file_path, os.path.basename(file_path))
                
        return FileResponse(
            path = temp_zip.name,
            filename = "files.zip",
            media_type = "application/zip",
            headers={"Content-Disposition": "attachment; filename=files.zip"}
        )
    
    
#파일 목록 조회
@app.get("/files",
         tags=["파일 목록 조회"],
         description="페이징 처리, 검색 필터링 지원")
async def get_files(skip: int = 0, limit: int = 10, q: Optional[str] = None):
    upload_dir = "uploads"
    files = os.listdir(upload_dir)
    
    # 검색 필터링
    if q:
        files = [f for f in files if q in f]

    # 페이징 처리
    total = len(files)
    return {
        "total": total,
        "files": files[skip:skip+limit]
    }
    

#파일 삭제
@app.delete("/delete-files",
           tags=["파일 삭제"],
           description="단일/다중 파일 삭제")
async def delete_files(filenames: list[str] = Query(...)):
    upload_dir = "uploads"
    deleted_files = []
    #파일 삭제
    for filename in filenames:
        file_path = os.path.join(upload_dir, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            deleted_files.append(filename)
        else:
            raise HTTPException(
                status_code=404,
                detail=f"파일 {filename}을 찾을 수 없습니다."
            )
    #삭제 성공 메시지 반환
    return {
        "message": "파일 삭제 성공",
        "deleted_files": deleted_files
    }

