const VueLoaderPlugin = require('vue-loader/lib/plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const path = require('path');


module.exports = {
    entry: {
        main: 'main.ts',
        author: 'author.ts',
    },
    mode: 'development',
    output: {
        path: path.resolve(__dirname, 'static'),
        filename: '[name].js',
    },
    module: {
        rules: [
            // ... другие правила
            {
                test: /\.vue$/,
                loader: 'vue-loader',
            },
            {
                test: /\.ts$/,
                loader: 'ts-loader',
                options: {
                    appendTsSuffixTo: [/\.vue$/],
                },
            },
            // {
            //     test: /\.css/,
            //     use: [
            //         // MiniCssExtractPlugin.loader,
            //         'vue-style-loader',
            //         'style-loader',
            //
            //         'css-loader',
            //     ],
            // },
            {
                test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '[path][name].[ext]',
                        },
                    },
                ],
            },
            {
                test: /\.s?css/,
                use: [
                    //'style-loader',
                    MiniCssExtractPlugin.loader,
                    //'vue-style-loader',

                    {
                        loader: 'css-loader',
                        options: { sourceMap: true },
                    },
                    {
                        loader: 'sass-loader',
                        options: {
                            sourceMap: true,
                            implementation: require("sass"),
                        },
                    },
                ],
            },
        ],
    },
    resolve: {
        modules: [path.resolve(__dirname, 'src'), 'node_modules'],
    },
    plugins: [
        // убедитесь что подключили плагин!
        new VueLoaderPlugin(),
        new MiniCssExtractPlugin({
            filename: 'style.css',
        }),
    ],
};