function truncateString(str, num) {
    return str.length > num ? str.substring(0, num) + '...' : str;
}

console.log(truncateString("A-tisket a-tasket A green and yellow basket", 8));
