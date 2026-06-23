function CategoryFilter({ category, setCategory }) {
  return (
    <select
      value={category}
      onChange={(e) => setCategory(e.target.value)}
    >
      <option value="">All Categories</option>
      <option value="Electronics">Electronics</option>
      <option value="Books">Books</option>
      <option value="Fashion">Fashion</option>
      <option value="Sports">Sports</option>
      <option value="Home">Home</option>
    </select>
  );
}

export default CategoryFilter;