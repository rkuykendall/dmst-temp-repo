module.exports = {
    entry: './web/js/main.js',
    output: {
        path: require('path').resolve('./web'),
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            { test: /\.css$/, loader: 'style-loader!css-loader' }
        ]
    }
};
