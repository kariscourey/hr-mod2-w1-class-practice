let nums = [1,2,3,4]
let input = [

]

function double(n) {
    return n*2;
}

// let result = [];
// for (let n of numbers) {
//     result.push(double(n));
// }

// let result = nums.map(n => double(n));

// let result = nums.map(n => {
//     return n*2;
// })

// map returns list of same length as original; it's a translation
// ALWAYS creates a new object

// let result = nums.map(n => n*2)

// let result = nums.map(n => n*2).map(num => num + 100).map(x => `You are now ${x} years old`)

let result = nums.map(n => n*2)
    .map(num => num + 100)
    .map(x => `You are now ${x} years old`)

console.log(result);

let persons = [
    {
        firstname: 'Warren',
        lastname: 'Longmire',
        age: 33,
    },
    {
        firstname: 'Pie',
        lastname: 'Lil',
        age: 5,
    },
]

// let people = persons.map(p => ({...p, 'fullname': p.firstname + ' ' + p.lastname}))

let people = persons.map(p => ({...p, 'fullname': p.firstname + ' ' + p.lastname}))
// return persons.map(p => (<h1>{p.firstname}</h1>)) // need to use return in the context of react

console.log(people)
