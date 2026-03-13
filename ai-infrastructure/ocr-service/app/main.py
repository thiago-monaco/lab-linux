from fastapi import FastAPI, UploadFile, File, HTTPException
from paddleocr import PaddleOCR
import numpy as np
import cv2
import sys

app = FastAPI()
ocr = PaddleOCR(use_angle_cls=True, lang='pt')

@app.get("/")
async def root():
    return {"status": "IA rodando e pronta!"}

@app.post("/extract")
async def extract_text(file: UploadFile = File(...)):
    contents = await file.read()
    
    if file.filename.lower().endswith(".pdf"):
         return {"aviso": "PDF ainda nao suportado. Use PNG ou JPG."}

    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        raise HTTPException(status_code=400, detail="Imagem invalida")

    # Roda a IA
    result = ocr.ocr(img)

    # Debug para confirmar o que esta chegando
    print(f"DEBUG FINAL - Type: {type(result)} - Content: {result}", file=sys.stderr)

    dados_limpos = []
    
    # --- FUNCAO AUXILIAR PARA EXTRAIR DO DICIONARIO NOVO ---
    def processar_dicionario(d):
        itens = []
        if 'rec_texts' in d and 'rec_scores' in d:
            textos = d['rec_texts']
            scores = d['rec_scores']
            for t, s in zip(textos, scores):
                itens.append({"texto": t, "confianca": float(s)})
        return itens

    # --- LOGICA UNIVERSAL ---
    # CASO 1: O resultado e direto um Dicionario
    if isinstance(result, dict):
        dados_limpos.extend(processar_dicionario(result))
    
    # CASO 2: O resultado e uma Lista
    elif isinstance(result, list):
        for item in result:
            # Sub-caso A: A lista contem Dicionarios (O QUE ESTA ACONTECENDO AGORA)
            if isinstance(item, dict):
                dados_limpos.extend(processar_dicionario(item))
            
            # Sub-caso B: A lista contem Listas (Formato antigo)
            elif isinstance(item, list):
                for linha in item:
                    if len(linha) > 1 and isinstance(linha[1], (list, tuple)):
                        dados_limpos.append({
                            "texto": linha[1][0],
                            "confianca": float(linha[1][1])
                        })

    return {"data": dados_limpos}
