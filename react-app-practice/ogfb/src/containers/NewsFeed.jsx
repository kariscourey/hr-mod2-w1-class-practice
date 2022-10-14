import NewsItem from '../components/NewsItem';

function NewsFeed() {

    const jsonResponse = {
        'newsfeed': [
            {"name": 'Pie',
            "action": 'is snacking'},
            {"name": 'Po',
            "action": 'is napping'},
        ]
    };

    const data = jsonResponse['newsfeed'];

    return (
        <div className='NewsFeed'>

            {data.map(item => {
                return(<NewsItem name={item.name} action={item.action}/>)
            })}

        </div>
    )
}

export default NewsFeed;
