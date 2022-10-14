function NewsItem(props) {
    const {name, action} = props;
    return (
        <div className='NewsItem'>
            <h3>{name}</h3>
            <p>{action}</p>
        </div>
    );
}

export default NewsItem;
