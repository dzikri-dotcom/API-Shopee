from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

SHOPEE_API_URL = "https://shopee.com/api/v4/search/search_items?by=relevancy&limit=10&keyword=smartphone"

@app.get("/products")
def get_products():
    """
    Mengambil daftar produk dari Shopee API berdasarkan kata kunci
    """
    try:
        response = httpx.get(SHOPEE_API_URL)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/product/{product_id}")
def get_product_detail(product_id: int):
    """
    Mengambil detail produk berdasarkan ID dari Shopee API
    """
    try:
        response = httpx.get(f"https://shopee.com/api/v4/item/get?itemid={product_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/search")
def search_products(keyword: str):
    """
    Mencari produk berdasarkan kata kunci dari Shopee API
    """
    try:
        search_url = f"https://shopee.com/api/v4/search/search_items?by=relevancy&limit=10&keyword={keyword}"
        response = httpx.get(search_url)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
