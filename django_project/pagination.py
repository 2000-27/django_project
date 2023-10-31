def page(data, request):
    pages = request.query_params.get("page")
    pages = int(pages)
    per_page = 1
    offset = (pages - 1) * per_page
    paginated_data = data[offset : offset + per_page]
    data = {
        "details": paginated_data,
        "page_number": pages,
        "per_page": per_page,
        "total_record": len(data),
        "total_pages": len(data) // per_page,
        "sucess": True,
    }
    return data
