# 🔍 OCR Service: O Desafio do PDF com PaddleOCR

Este projeto é uma API de reconhecimento óptico de caracteres (OCR) de alta performance. O grande diferencial aqui não é apenas ler imagens, mas resolver a "treta" de processar arquivos PDF de forma eficiente.



---

## 🧠 A "Dor": Por que OCR em PDF é difícil?
A maioria das bibliotecas de IA (como PaddleOCR ou Tesseract) opera em **matrizes de pixels (imagens)**. Um PDF não é uma imagem; é um container de objetos. 

Se você tentar passar um PDF direto para a IA, ela vai retornar erro. Para resolver isso, criei um pipeline que faz a ponte entre o sistema operacional e o modelo de Deep Learning.

---

## 🛠️ O Fluxo da Solução (Passo a Passo)

### 1. Preparação da Infra (O Segredo)
O Python sozinho não consegue "desenhar" as páginas de um PDF. Ele precisa do **Poppler**, um motor de renderização de PDF do mundo Linux. 
No Dockerfile, garantimos essa instalação:
```bash
apt-get install -y poppler-utils

### 2. Recepção e Validação (FastAPI)
O arquivo entra via endpoint `POST`. O FastAPI utiliza o `python-multipart` para receber o arquivo binário. O sistema identifica se o arquivo é um PDF ou uma imagem comum e inicia o tratamento adequado.

### 3. O Pipeline de Conversão (`pdf2image`)
Se o arquivo for um PDF, o serviço inicia a **rasterização**:
* **Conversão:** O `pdf2image` transforma cada página do PDF em uma imagem de alta resolução na memória RAM.
* **Resolução:** Ajustamos o DPI para garantir que textos pequenos sejam detectados com precisão pela IA.

### 4. Inteligência Visual (PaddleOCR)
Com as imagens prontas, o **PaddleOCR** (IA da Baidu) assume o comando:
1.  **Detecção de Texto:** Localiza onde há blocos de escrita.
2.  **Classificação de Ângulo:** Corrige automaticamente se o documento foi escaneado torto.
3.  **Reconhecimento (OCR):** Converte os pixels em caracteres reais com precisão superior ao Tesseract tradicional.

### 5. Entrega de Dados
O texto extraído é estruturado e devolvido via JSON, organizado por páginas, pronto para ser consumido por outros sistemas ou bancos de dados.

---

## 🚀 Como Instalar e Rodar

### Opção A: Docker (Recomendado)
O Docker já configura o Poppler e todas as bibliotecas Python automaticamente.
```bash
# Entre na pasta do serviço
cd ai-infrastructure/ocr-service

# Suba o container
docker-compose up -d

Durante o desenvolvimento, notei dois pontos que fazem toda a diferença:

DPI de Conversão: Usar 200 ou 300 DPI no pdf2image é o equilíbrio ideal entre precisão e velocidade. Menos que isso, a IA "alucina" caracteres.

Memória RAM: O PaddleOCR com arquivos PDF pesados pode consumir bastante memória. Se rodar em ambiente limitado, considere processar as páginas uma a uma em vez de carregar o PDF inteiro.

📝 Exemplo de Uso (cURL)
Teste sua API rapidamente via terminal:

Bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@seu_documento.pdf'
🎯 Conclusão e Portfólio
Este projeto demonstra não apenas a aplicação de Inteligência Artificial, mas principalmente a capacidade de Engenharia de Software para resolver limitações nativas de bibliotecas, criando um pipeline robusto que integra:

Infraestrutura Linux (Poppler/Binários)

Containerização (Docker)

Backend Moderno (FastAPI)

IA de Ponta (PaddleOCR)
