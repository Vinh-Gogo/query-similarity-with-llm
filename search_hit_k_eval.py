import random
import pandas as pd

# --------------------------
# Prompt templates
# --------------------------
prompts = [
    "Tôi muốn mua {product_name}, bên bạn còn hàng không?",
    "Cho tôi hỏi {product_name} hiện tại giá bao nhiêu?",
    "Tôi đang quan tâm đến {product_name}, bạn có thể tư vấn thêm cho tôi không?",
    "{product_name} có màu nào và dung lượng bao nhiêu GB vậy?",
    "Tôi muốn đặt mua {product_name}, cần làm thế nào?"
]

def get_random_prompt(product_name: str) -> str:
    return random.choice(prompts).format(product_name=product_name)

# --------------------------
# Stub search (replace later)
# --------------------------
def hybrid_search(prompt: str, k: int):
    """
    Trả về list top-k kết quả (dict với _id).
    Bạn sẽ thay bằng search thực tế.
    """
    return [{"_id": "demo_id"} for _ in range(k)]

# --------------------------
# Benchmark for dataframe
# --------------------------
def benchmark_df(df: pd.DataFrame, ks=(1, 5, 10)):
    results = {f"hit@{k}": 0 for k in ks}
    total = len(df)

    for _, row in df.iterrows():
        ground_truth_id = row["_id"]
        # nếu bạn muốn lấy tên từ "title", thì thay "product_name" bằng "title"
        product_name = row.get("product_name") or row["title"].split("-")[0].strip()
        
        query = get_random_prompt(product_name)
        print(f"[TEST] id={ground_truth_id} | query='{query}'")

        for k in ks:
            retrieved = hybrid_search(query, k)
            if any(r["_id"] == ground_truth_id for r in retrieved):
                results[f"hit@{k}"] += 1

    for k in ks:
        results[f"hit@{k}"] /= total

    return results


# --------------------------
# Demo
# --------------------------
if __name__ == "__main__":
    # CSV thực tế
    df = pd.read_csv("hoanghamobile.csv")

    scores = benchmark_df(df)
    print("\nFinal scores:", scores)
