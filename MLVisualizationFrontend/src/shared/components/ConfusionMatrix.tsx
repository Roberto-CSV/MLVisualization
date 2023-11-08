export interface ConfusionMatrixInterface {
    truePositive: number,
    falseNegative: number
    falsePositive: number,
    trueNegative: number,
}

export const ConfusionMatrixTypes = {
    TRUE_POSITIVE: {
        name: 'Verdadero positivo',
        shortName: 'VP'
    },
    FALSE_NEGATIVE: {
        name: 'Falso negativo',
        shortName: 'FN'
    },
    FALSE_POSITIVE: {
        name: 'Falso positivo',
        shortName: 'FP'
    },
    TRUE_NEGATIVE: {
        name: 'Verdadero negativo',
        shortName: 'VN'
    }
}

export const ConfusionMatrix = ({ data }) => {
    const confusionMatrix: ConfusionMatrixInterface = data;
    const elementsQuantity: number = confusionMatrix.truePositive
        + confusionMatrix.falsePositive
        + confusionMatrix.trueNegative
        + confusionMatrix.falseNegative
    const getTypeBackgroundColor = (quantity: number) => {
        let backgroundColor: string = '';
        const percentile: number = quantity / elementsQuantity;
        if (percentile >= 0.8) {
            backgroundColor = 'bg-danger';
        } else if (percentile >= 0.6) {
            backgroundColor = 'bg-warning-subtle';
        } else if (percentile >= 0.3) {
            backgroundColor = 'bg-success-subtle';
        } else {
            backgroundColor = 'bg-primary-subtle';
        }
        return backgroundColor;
    }
    const confusionMatrixBGColors = {
        truePositive: getTypeBackgroundColor(confusionMatrix.truePositive),
        falseNegative: getTypeBackgroundColor(confusionMatrix.falseNegative),
        falsePositive: getTypeBackgroundColor(confusionMatrix.falsePositive),
        trueNegative: getTypeBackgroundColor(confusionMatrix.trueNegative)
    }

    return (
        <table className="table table-bordered text-center align-middle">
            <tbody>
                <tr>
                    <td className={'p-5 opacity-100 ' + confusionMatrixBGColors.truePositive}>
                        <p>{confusionMatrix.truePositive}</p>
                    </td>
                    <td className={'p-5 opacity-100 ' + confusionMatrixBGColors.falseNegative}>
                        <p>{confusionMatrix.falseNegative}</p>
                    </td>
                </tr>
                <tr>
                    <td className={'p-5 opacity-100 ' + confusionMatrixBGColors.falsePositive}>
                        <p>{confusionMatrix.falsePositive}</p>
                    </td>
                    <td className={'p-5 opacity-100 ' + confusionMatrixBGColors.trueNegative}>
                        <p>{confusionMatrix.trueNegative}</p>
                    </td>
                </tr>
            </tbody>
        </table>
    )
}
