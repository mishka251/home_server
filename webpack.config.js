// webpack.config.js
const VueLoaderPlugin = require('vue-loader/lib/plugin');

const path = require('path');

module.exports = {
    entry: {
        main: 'main.ts',
        author: 'author.ts',
    },
    mode: 'development',
    output: {
        path: path.resolve(__dirname, 'static'),
        filename: '[name].js'
    },
    module: {
        rules: [
            // ... другие правила
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.ts$/,
                loader: 'ts-loader',
                options: {
                    appendTsSuffixTo: [/\.vue$/],
                }
            },
            {
                test: /\.css/,
                loaders: [
                    'vue-style-loader',
                    'css-loader'
                ]
            }
        ]
    },
    resolve: {
        modules: [path.resolve(__dirname, 'src'), 'node_modules']
    },
    plugins: [
        // убедитесь что подключили плагин!
        new VueLoaderPlugin()
    ]
};