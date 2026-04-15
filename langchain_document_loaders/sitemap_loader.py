from langchain_community.document_loaders import SitemapLoader

loader = SitemapLoader(
    web_path="https://pc.scasf.com/page-sitemap.xml",
    max_depth=100
    )

docs = loader.load()

for document in docs:
    print(document.page_content)
    print("metadata: ", document.metadata)


# import json
# from langchain_community.document_loaders import SitemapLoader

# loader = SitemapLoader(
#     web_path="https://pc.scasf.com/sitemap_index.xml",
#     max_depth=100
# )

# docs = list(loader.lazy_load())  # convert generator → list

# data = [
#     {
#         "content": doc.page_content,
#         "metadata": doc.metadata
#     }
#     for doc in docs
# ]

# with open("documents_v2.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=2, ensure_ascii=False)

# print("Saved to documents.json")