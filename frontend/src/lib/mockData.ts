import { Organization, Workspace, Project, ProjectFile, MigrationLog, User, MigrationBatch, LLMProviderType } from './types';

export const mockUser: User = {
  id: 'user-1', name: 'Harsh Patel', email: 'admin@MigrationStudio.io', role: 'admin', avatar: '',
};

export const mockOrganizations: Organization[] = [
  { id: 'org-1', name: 'Acme Corporation', description: 'Enterprise integration platform migration', owner: 'Harsh Patel', createdAt: '2026-01-15', workspaceCount: 3, logo: '' },
  { id: 'org-2', name: 'TechFlow Inc', description: 'API modernization initiative', owner: 'Sarah Chen', createdAt: '2026-02-01', workspaceCount: 2, logo: '' },
  { id: 'org-3', name: 'DataBridge Solutions', description: 'Legacy system migration to cloud-native', owner: 'Alex Kumar', createdAt: '2026-02-10', workspaceCount: 1, logo: '' },
];

export const mockWorkspaces: Workspace[] = [
  { id: 'ws-1', orgId: 'org-1', name: 'Development', environment: 'dev', memberCount: 8, projectCount: 4 },
  { id: 'ws-2', orgId: 'org-1', name: 'Staging', environment: 'test', memberCount: 5, projectCount: 3 },
  { id: 'ws-3', orgId: 'org-1', name: 'Production', environment: 'prod', memberCount: 3, projectCount: 2 },
  { id: 'ws-4', orgId: 'org-2', name: 'Dev Environment', environment: 'dev', memberCount: 6, projectCount: 3 },
  { id: 'ws-5', orgId: 'org-2', name: 'Production', environment: 'prod', memberCount: 4, projectCount: 2 },
];

export const mockProjects: Project[] = [
  { id: 'proj-1', workspaceId: 'ws-1', orgId: 'org-1', name: 'Order Processing API', description: 'Migrate order processing Mule flows to AWS Lambda', migrationType: 'mule4-lambda', targetRuntime: 'nodejs', sourceType: 'git', status: 'in-progress', totalFiles: 12, migratedFiles: 8, failedFiles: 1, migrationRuns: 0, createdAt: '2026-02-12', lastActivity: '2026-02-22' },
  { id: 'proj-2', workspaceId: 'ws-1', orgId: 'org-1', name: 'Customer Data Sync', description: 'Migrate customer data synchronization batch jobs', migrationType: 'batch-stepfunction', targetRuntime: 'python', sourceType: 'zip', status: 'completed', totalFiles: 12, migratedFiles: 12, failedFiles: 0, migrationRuns: 0, createdAt: '2026-01-28', lastActivity: '2026-02-18' },
  { id: 'proj-3', workspaceId: 'ws-1', orgId: 'org-1', name: 'Payment Gateway', description: 'Migrate payment processing APIs', migrationType: 'apiled-apigateway', targetRuntime: 'nodejs', sourceType: 'git', status: 'pending', totalFiles: 18, migratedFiles: 0, failedFiles: 0, migrationRuns: 0, createdAt: '2026-02-20', lastActivity: '2026-02-20' },
];

/* ─────────────────────────────────────────────────────────────────
   File Tree — realistic MuleSoft 4 project structure
   Folders use `children` refs, files use content + migratedContent
   ───────────────────────────────────────────────────────────────── */

// Store expected migrated content separately — migration engine will populate files from this map
const _migratedContentStore: Record<string, string> = {};

const F = (id: string, projectId: string, name: string, path: string, lang: string, _status: 'pending' | 'in-progress' | 'completed' | 'failed', content: string, migratedContent: string, size = 0): ProjectFile => {
  // Save expected migrated content for the migration engine to use later
  if (migratedContent) _migratedContentStore[id] = migratedContent;
  return {
    id, projectId, name, path, type: 'file', language: lang,
    status: 'pending',           // Always start as pending (fresh import)
    content,
    migratedContent: '',         // Empty until migration runs
    children: [], size: size || content.length, lastModified: '2026-02-22T10:00:00Z',
  };
};

const D = (id: string, projectId: string, name: string, path: string, children: string[]): ProjectFile => ({
  id, projectId, name, path, type: 'folder', language: '', status: 'in-progress', content: '', migratedContent: '', children, size: 0, lastModified: '2026-02-22T10:00:00Z',
});

export const mockFiles: ProjectFile[] = [
  // ── Root folders ──
  D('root', 'proj-1', 'Order Processing API', '/', ['f-src', 'f-api', 'f-resources', 'f-test', 'f-root-pom', 'f-root-artifact', 'f-root-readme']),
  D('f-src', 'proj-1', 'src', '/src', ['f-src-main']),
  D('f-src-main', 'proj-1', 'main', '/src/main', ['f-mule', 'f-dwl']),

  // ── Source MuleSoft flows ──
  D('f-mule', 'proj-1', 'mule', '/src/main/mule', ['f-order-flow', 'f-inventory-flow', 'f-notification-flow', 'f-error-handler', 'f-global-config']),

  F('f-order-flow', 'proj-1', 'order-process-flow.xml', '/src/main/mule/order-process-flow.xml', 'xml', 'completed',
    `<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:http="http://www.mulesoft.org/schema/mule/http"
      xmlns:db="http://www.mulesoft.org/schema/mule/db"
      xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core">

  <http:listener-config name="HTTP_Listener" host="0.0.0.0" port="8081"/>
  <db:config name="Database_Config">
    <db:my-sql-connection host="\${db.host}" port="3306"
      user="\${db.user}" password="\${db.password}" database="orders"/>
  </db:config>

  <flow name="getOrdersFlow">
    <http:listener config-ref="HTTP_Listener" path="/api/orders" method="GET"/>
    <logger level="INFO" message="Fetching all orders"/>
    <db:select config-ref="Database_Config">
      <db:sql>SELECT * FROM orders ORDER BY created_at DESC LIMIT 100</db:sql>
    </db:select>
    <ee:transform>
      <ee:message>
        <ee:set-payload><![CDATA[%dw 2.0
output application/json
---
payload map (order) -> {
  orderId: order.id,
  customerName: order.customer_name,
  amount: order.total_amount,
  status: order.status,
  createdAt: order.created_at
}]]></ee:set-payload>
      </ee:message>
    </ee:transform>
  </flow>

  <flow name="createOrderFlow">
    <http:listener config-ref="HTTP_Listener" path="/api/orders" method="POST"/>
    <logger level="INFO" message="Creating order: #[payload]"/>
    <set-variable variableName="orderId" value="#[uuid()]"/>
    <db:insert config-ref="Database_Config">
      <db:sql>INSERT INTO orders (id, customer_name, total_amount, status)
              VALUES (:id, :name, :amount, 'pending')</db:sql>
      <db:input-parameters>#[{
        id: vars.orderId,
        name: payload.customerName,
        amount: payload.amount
      }]</db:input-parameters>
    </db:insert>
    <ee:transform>
      <ee:message>
        <ee:set-payload><![CDATA[%dw 2.0
output application/json
---
{ orderId: vars.orderId, status: "created" }]]></ee:set-payload>
      </ee:message>
    </ee:transform>
  </flow>

  <flow name="getOrderByIdFlow">
    <http:listener config-ref="HTTP_Listener" path="/api/orders/{orderId}" method="GET"/>
    <set-variable variableName="orderId" value="#[attributes.uriParams.orderId]"/>
    <db:select config-ref="Database_Config">
      <db:sql>SELECT * FROM orders WHERE id = :orderId</db:sql>
      <db:input-parameters>#[{ orderId: vars.orderId }]</db:input-parameters>
    </db:select>
    <choice>
      <when expression="#[sizeOf(payload) > 0]">
        <ee:transform>
          <ee:message>
            <ee:set-payload><![CDATA[%dw 2.0
output application/json
---
payload[0]]]></ee:set-payload>
          </ee:message>
        </ee:transform>
      </when>
      <otherwise>
        <set-payload value='#[{ "error": "Order not found" }]'/>
        <set-variable variableName="httpStatus" value="404"/>
      </otherwise>
    </choice>
  </flow>
</mule>`,
    `// Lambda Handler — Order Processing (migrated from order-process-flow.xml)
const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, ScanCommand, PutCommand, GetCommand } = require('@aws-sdk/lib-dynamodb');
const { v4: uuid } = require('uuid');

const client = new DynamoDBClient({});
const dynamo = DynamoDBDocumentClient.from(client);
const TABLE = process.env.ORDERS_TABLE || 'orders';

exports.handler = async (event) => {
  const method = event.httpMethod || event.requestContext?.http?.method;
  const pathParams = event.pathParameters || {};

  try {
    switch (method) {
      case 'GET':
        return pathParams.orderId
          ? await getOrderById(pathParams.orderId)
          : await getOrders();

      case 'POST':
        return await createOrder(JSON.parse(event.body));

      default:
        return response(405, { error: 'Method not allowed' });
    }
  } catch (err) {
    console.error('Order processing error:', err);
    return response(500, { error: err.message });
  }
};

async function getOrders() {
  const result = await dynamo.send(new ScanCommand({
    TableName: TABLE,
    Limit: 100,
  }));
  // Transform — equivalent to DataWeave mapping
  const orders = (result.Items || []).map(order => ({
    orderId: order.id,
    customerName: order.customer_name,
    amount: order.total_amount,
    status: order.status,
    createdAt: order.created_at,
  }));
  return response(200, orders);
}

async function getOrderById(orderId) {
  const result = await dynamo.send(new GetCommand({
    TableName: TABLE,
    Key: { id: orderId },
  }));
  if (!result.Item) {
    return response(404, { error: 'Order not found' });
  }
  return response(200, result.Item);
}

async function createOrder(body) {
  const orderId = uuid();
  await dynamo.send(new PutCommand({
    TableName: TABLE,
    Item: {
      id: orderId,
      customer_name: body.customerName,
      total_amount: body.amount,
      status: 'pending',
      created_at: new Date().toISOString(),
    },
  }));
  return response(201, { orderId, status: 'created' });
}

function response(statusCode, body) {
  return {
    statusCode,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  };
}`),

  F('f-inventory-flow', 'proj-1', 'inventory-check-flow.xml', '/src/main/mule/inventory-check-flow.xml', 'xml', 'completed',
    `<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:http="http://www.mulesoft.org/schema/mule/http">

  <flow name="checkInventoryFlow">
    <http:listener config-ref="HTTP_Listener" path="/api/inventory/{productId}" method="GET"/>
    <logger level="INFO" message="Checking inventory for: #[attributes.uriParams.productId]"/>
    <http:request method="GET"
      url="http://inventory-service:8082/stock/#[attributes.uriParams.productId]"/>
    <choice>
      <when expression="#[payload.quantity > 0]">
        <set-payload value='#[{ available: true, quantity: payload.quantity }]'/>
      </when>
      <otherwise>
        <set-payload value='#[{ available: false, quantity: 0 }]'/>
      </otherwise>
    </choice>
  </flow>
</mule>`,
    `// Lambda Handler — Inventory Check (migrated from inventory-check-flow.xml)
const https = require('https');

exports.handler = async (event) => {
  const productId = event.pathParameters?.productId;
  console.log('Checking inventory for:', productId);

  try {
    const stockData = await fetchStock(productId);
    const result = stockData.quantity > 0
      ? { available: true, quantity: stockData.quantity }
      : { available: false, quantity: 0 };

    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(result),
    };
  } catch (err) {
    console.error('Inventory check failed:', err);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: err.message }),
    };
  }
};

function fetchStock(productId) {
  const url = \`\${process.env.INVENTORY_SERVICE_URL}/stock/\${productId}\`;
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(JSON.parse(data)));
    }).on('error', reject);
  });
}`),

  F('f-notification-flow', 'proj-1', 'notification-flow.xml', '/src/main/mule/notification-flow.xml', 'xml', 'completed',
    `<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:email="http://www.mulesoft.org/schema/mule/email">

  <email:smtp-config name="SMTP_Config" host="\${smtp.host}" port="587"/>

  <flow name="sendOrderConfirmationFlow">
    <set-variable variableName="orderDetails" value="#[payload]"/>
    <email:send config-ref="SMTP_Config">
      <email:to-addresses>
        <email:to-address value="#[vars.orderDetails.customerEmail]"/>
      </email:to-addresses>
      <email:body contentType="text/html">
        <email:content><![CDATA[
          <h1>Order Confirmed</h1>
          <p>Your order #[vars.orderDetails.orderId] has been confirmed.</p>
          <p>Total: $#[vars.orderDetails.amount]</p>
        ]]></email:content>
      </email:body>
    </email:send>
    <logger level="INFO" message="Notification sent for order: #[vars.orderDetails.orderId]"/>
  </flow>
</mule>`,
    `// Lambda Handler — Notification (migrated from notification-flow.xml)
const { SESClient, SendEmailCommand } = require('@aws-sdk/client-ses');

const ses = new SESClient({});

exports.handler = async (event) => {
  const orderDetails = typeof event.body === 'string'
    ? JSON.parse(event.body) : event;

  console.log('Sending notification for order:', orderDetails.orderId);

  try {
    await ses.send(new SendEmailCommand({
      Source: process.env.FROM_EMAIL || 'noreply@example.com',
      Destination: {
        ToAddresses: [orderDetails.customerEmail],
      },
      Message: {
        Subject: { Data: 'Order Confirmed' },
        Body: {
          Html: {
            Data: \`
              <h1>Order Confirmed</h1>
              <p>Your order \${orderDetails.orderId} has been confirmed.</p>
              <p>Total: $\${orderDetails.amount}</p>
            \`,
          },
        },
      },
    }));

    console.log('Notification sent for order:', orderDetails.orderId);
    return { statusCode: 200, body: JSON.stringify({ sent: true }) };
  } catch (err) {
    console.error('Failed to send notification:', err);
    return { statusCode: 500, body: JSON.stringify({ error: err.message }) };
  }
};`),

  F('f-error-handler', 'proj-1', 'global-error-handler.xml', '/src/main/mule/global-error-handler.xml', 'xml', 'failed',
    `<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core">
  <error-handler name="globalErrorHandler">
    <on-error-propagate type="HTTP:UNAUTHORIZED">
      <set-variable variableName="httpStatus" value="401"/>
      <set-payload value='#[{ "error": "Unauthorized", "code": 401 }]'/>
    </on-error-propagate>
    <on-error-propagate type="HTTP:NOT_FOUND">
      <set-variable variableName="httpStatus" value="404"/>
      <set-payload value='#[{ "error": "Not Found", "code": 404 }]'/>
    </on-error-propagate>
    <on-error-propagate type="DB:CONNECTIVITY">
      <logger level="ERROR" message="Database connection failed: #[error.description]"/>
      <set-payload value='#[{ "error": "Service unavailable" }]'/>
    </on-error-propagate>
    <on-error-continue type="ANY">
      <logger level="ERROR" message="Unhandled error: #[error.description]"/>
      <set-payload value='#[{ "error": error.description }]'/>
    </on-error-continue>
  </error-handler>
</mule>`,
    `// ⚠ MIGRATION FAILED — Manual review required
// The following error handler mappings could not be automatically migrated:
// - HTTP:UNAUTHORIZED → needs custom authorizer integration
// - DB:CONNECTIVITY → needs DynamoDB-specific error handling
//
// TODO: Implement error handling middleware
// See: https://docs.aws.amazon.com/lambda/latest/dg/nodejs-exceptions.html

class MigrationError extends Error {
  constructor(message, statusCode = 500) {
    super(message);
    this.statusCode = statusCode;
  }
}

function errorResponse(error) {
  const statusCode = error.statusCode || 500;
  const message = error.message || 'Internal Server Error';

  return {
    statusCode,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ error: message, code: statusCode }),
  };
}

module.exports = { MigrationError, errorResponse };`),

  F('f-global-config', 'proj-1', 'global-config.xml', '/src/main/mule/global-config.xml', 'xml', 'completed',
    `<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core">
  <configuration-properties file="config.properties"/>
  <global-property name="http.port" value="8081"/>
  <global-property name="api.basePath" value="/api"/>
  <global-property name="db.host" value="localhost"/>
  <global-property name="db.user" value="admin"/>
  <global-property name="db.password" value="secret"/>
  <global-property name="smtp.host" value="smtp.example.com"/>
</mule>`,
    `// Environment Configuration (migrated from global-config.xml)
// In AWS Lambda, these become environment variables set in SAM/CloudFormation

module.exports = {
  httpPort: process.env.HTTP_PORT || 8081,
  apiBasePath: process.env.API_BASE_PATH || '/api',
  db: {
    tableName: process.env.ORDERS_TABLE || 'orders',
    region: process.env.AWS_REGION || 'us-east-2',
  },
  email: {
    fromAddress: process.env.FROM_EMAIL || 'noreply@example.com',
    region: process.env.SES_REGION || 'us-east-2',
  },
  stage: process.env.STAGE || 'dev',
};`),

  // ── DataWeave Transforms ──
  D('f-dwl', 'proj-1', 'dwl', '/src/main/dwl', ['f-transform-order', 'f-transform-response']),

  F('f-transform-order', 'proj-1', 'transform-order.dwl', '/src/main/dwl/transform-order.dwl', 'plaintext', 'completed',
    `%dw 2.0
output application/json

fun formatCurrency(amount: Number): String =
  "$" ++ (amount as String {format: "#,##0.00"})

---
{
  orderId: payload.id,
  customer: {
    name: payload.customer_name,
    email: payload.customer_email
  },
  items: payload.items map (item) -> {
    productId: item.product_id,
    name: item.product_name,
    quantity: item.qty,
    price: formatCurrency(item.unit_price),
    subtotal: formatCurrency(item.qty * item.unit_price)
  },
  total: formatCurrency(payload.total_amount),
  status: upper(payload.status),
  createdAt: payload.created_at as DateTime
}`,
    `// transform-order.js (migrated from transform-order.dwl)

function formatCurrency(amount) {
  return '$' + amount.toLocaleString('en-US', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
}

function transformOrder(payload) {
  return {
    orderId: payload.id,
    customer: {
      name: payload.customer_name,
      email: payload.customer_email,
    },
    items: (payload.items || []).map(item => ({
      productId: item.product_id,
      name: item.product_name,
      quantity: item.qty,
      price: formatCurrency(item.unit_price),
      subtotal: formatCurrency(item.qty * item.unit_price),
    })),
    total: formatCurrency(payload.total_amount),
    status: (payload.status || '').toUpperCase(),
    createdAt: new Date(payload.created_at).toISOString(),
  };
}

module.exports = { transformOrder, formatCurrency };`),

  F('f-transform-response', 'proj-1', 'api-response.dwl', '/src/main/dwl/api-response.dwl', 'plaintext', 'in-progress',
    `%dw 2.0
output application/json

fun buildResponse(statusCode: Number, body: Any): Object = {
  statusCode: statusCode,
  headers: {
    "Content-Type": "application/json",
    "X-Request-Id": uuid()
  },
  body: write(body, "application/json")
}

---
buildResponse(200, payload)`,
    `// api-response.js (migrated from api-response.dwl)
const { v4: uuid } = require('uuid');

function buildResponse(statusCode, body) {
  return {
    statusCode,
    headers: {
      'Content-Type': 'application/json',
      'X-Request-Id': uuid(),
      'Access-Control-Allow-Origin': '*',
    },
    body: JSON.stringify(body),
  };
}

module.exports = { buildResponse };`),

  // ── API spec ──
  D('f-api', 'proj-1', 'api', '/api', ['f-api-spec']),

  F('f-api-spec', 'proj-1', 'orders-api.raml', '/api/orders-api.raml', 'yaml', 'in-progress',
    `#%RAML 1.0
title: Orders API
version: v1
baseUri: http://api.example.com/{version}
mediaType: application/json

types:
  Order:
    properties:
      orderId: string
      customerName: string
      amount: number
      status:
        enum: [pending, confirmed, shipped, delivered, cancelled]
      createdAt: datetime

  OrderCreateRequest:
    properties:
      customerName: string
      customerEmail: string
      amount: number
      items:
        type: array
        items:
          properties:
            productId: string
            quantity: integer
            unitPrice: number

/orders:
  get:
    description: List all orders
    queryParameters:
      status:
        required: false
        type: string
      limit:
        required: false
        type: integer
        default: 100
    responses:
      200:
        body: Order[]
  post:
    description: Create a new order
    body: OrderCreateRequest
    responses:
      201:
        body: Order
  /{orderId}:
    get:
      description: Get order by ID
      responses:
        200:
          body: Order
        404:
          body:
            properties:
              error: string`,
    `# API Gateway — OpenAPI 3.0 (migrated from orders-api.raml)
openapi: 3.0.1
info:
  title: Orders API
  version: v1
  description: Order Processing API — migrated from MuleSoft RAML
paths:
  /orders:
    get:
      summary: List all orders
      parameters:
        - name: status
          in: query
          schema: { type: string }
        - name: limit
          in: query
          schema: { type: integer, default: 100 }
      x-amazon-apigateway-integration:
        type: aws_proxy
        httpMethod: POST
        uri: !Sub arn:aws:apigateway:\${AWS::Region}:lambda:path/2015-03-31/functions/\${OrderFunction.Arn}/invocations
      responses:
        '200':
          description: Success
    post:
      summary: Create a new order
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrderCreateRequest'
      x-amazon-apigateway-integration:
        type: aws_proxy
        httpMethod: POST
        uri: !Sub arn:aws:apigateway:\${AWS::Region}:lambda:path/2015-03-31/functions/\${OrderFunction.Arn}/invocations
      responses:
        '201':
          description: Created
  /orders/{orderId}:
    get:
      summary: Get order by ID
      parameters:
        - name: orderId
          in: path
          required: true
          schema: { type: string }
      x-amazon-apigateway-integration:
        type: aws_proxy
        httpMethod: POST
        uri: !Sub arn:aws:apigateway:\${AWS::Region}:lambda:path/2015-03-31/functions/\${OrderFunction.Arn}/invocations
      responses:
        '200':
          description: Success
        '404':
          description: Not found
components:
  schemas:
    OrderCreateRequest:
      type: object
      required: [customerName, customerEmail, amount]
      properties:
        customerName: { type: string }
        customerEmail: { type: string, format: email }
        amount: { type: number }
        items:
          type: array
          items:
            type: object
            properties:
              productId: { type: string }
              quantity: { type: integer }
              unitPrice: { type: number }`),

  // ── Resources / config ──
  D('f-resources', 'proj-1', 'resources', '/resources', ['f-config-props', 'f-log4j']),

  F('f-config-props', 'proj-1', 'config.properties', '/resources/config.properties', 'plaintext', 'completed',
    `# MuleSoft Configuration Properties
http.port=8081
api.basePath=/api
db.host=localhost
db.port=3306
db.user=admin
db.password=\${secure::db.password}
db.database=orders
smtp.host=smtp.example.com
smtp.port=587`,
    `# AWS Lambda Environment Variables (.env template)
# These should be set in your SAM template or CloudFormation parameters

ORDERS_TABLE=orders
AWS_REGION=us-east-2
FROM_EMAIL=noreply@example.com
SES_REGION=us-east-2
INVENTORY_SERVICE_URL=https://inventory-api.internal
STAGE=dev
LOG_LEVEL=info`),

  F('f-log4j', 'proj-1', 'log4j2.xml', '/resources/log4j2.xml', 'xml', 'completed',
    `<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
  <Appenders>
    <Console name="Console" target="SYSTEM_OUT">
      <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m%n"/>
    </Console>
  </Appenders>
  <Loggers>
    <Root level="INFO">
      <AppenderRef ref="Console"/>
    </Root>
    <Logger name="org.mule" level="INFO"/>
  </Loggers>
</Configuration>`,
    `// Logger configuration (migrated from log4j2.xml)
// AWS Lambda uses CloudWatch Logs natively via console.log/error/warn

const LOG_LEVEL = process.env.LOG_LEVEL || 'info';
const levels = { error: 0, warn: 1, info: 2, debug: 3 };

const logger = {
  error: (...args) => console.error(new Date().toISOString(), '[ERROR]', ...args),
  warn:  (...args) => levels[LOG_LEVEL] >= 1 && console.warn(new Date().toISOString(), '[WARN]', ...args),
  info:  (...args) => levels[LOG_LEVEL] >= 2 && console.log(new Date().toISOString(), '[INFO]', ...args),
  debug: (...args) => levels[LOG_LEVEL] >= 3 && console.log(new Date().toISOString(), '[DEBUG]', ...args),
};

module.exports = logger;`),

  // ── Tests ──
  D('f-test', 'proj-1', 'test', '/test', ['f-test-orders', 'f-test-inventory']),

  F('f-test-orders', 'proj-1', 'order-test-suite.xml', '/test/order-test-suite.xml', 'xml', 'pending',
    `<?xml version="1.0" encoding="UTF-8"?>
<munit:config name="order-test-suite"
  xmlns:munit="http://www.mulesoft.org/schema/mule/munit">

  <munit:test name="test-createOrder-success">
    <munit:execution>
      <http:request method="POST" url="http://localhost:8081/api/orders">
        <http:body><![CDATA[{
          "customerName": "John Doe",
          "amount": 99.99
        }]]></http:body>
      </http:request>
    </munit:execution>
    <munit:validation>
      <munit:assert-that expression="#[attributes.statusCode]" is="#[equalTo(201)]"/>
    </munit:validation>
  </munit:test>

  <munit:test name="test-getOrder-notFound">
    <munit:execution>
      <http:request method="GET" url="http://localhost:8081/api/orders/nonexistent"/>
    </munit:execution>
    <munit:validation>
      <munit:assert-that expression="#[attributes.statusCode]" is="#[equalTo(404)]"/>
    </munit:validation>
  </munit:test>
</munit:config>`,
    ``),

  F('f-test-inventory', 'proj-1', 'inventory-test-suite.xml', '/test/inventory-test-suite.xml', 'xml', 'pending',
    `<?xml version="1.0" encoding="UTF-8"?>
<munit:config name="inventory-test-suite"
  xmlns:munit="http://www.mulesoft.org/schema/mule/munit">

  <munit:test name="test-checkInventory-available">
    <munit:execution>
      <http:request method="GET" url="http://localhost:8081/api/inventory/PROD-001"/>
    </munit:execution>
    <munit:validation>
      <munit:assert-that expression="#[payload.available]" is="#[equalTo(true)]"/>
    </munit:validation>
  </munit:test>
</munit:config>`,
    ``),

  // ── Root files ──
  F('f-root-pom', 'proj-1', 'pom.xml', '/pom.xml', 'xml', 'completed',
    `<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.acme</groupId>
  <artifactId>order-processing</artifactId>
  <version>1.0.0</version>
  <packaging>mule-application</packaging>

  <properties>
    <mule.version>4.4.0</mule.version>
    <munit.version>2.3.13</munit.version>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.mule.connectors</groupId>
      <artifactId>mule-http-connector</artifactId>
      <version>1.7.3</version>
    </dependency>
    <dependency>
      <groupId>org.mule.connectors</groupId>
      <artifactId>mule-db-connector</artifactId>
      <version>1.13.6</version>
    </dependency>
    <dependency>
      <groupId>org.mule.connectors</groupId>
      <artifactId>mule-email-connector</artifactId>
      <version>1.6.3</version>
    </dependency>
  </dependencies>
</project>`,
    `{
  "name": "order-processing-lambda",
  "version": "1.0.0",
  "description": "Order Processing API — Migrated from MuleSoft 4",
  "main": "src/handlers/order-handler.js",
  "scripts": {
    "test": "jest",
    "deploy": "sam deploy --guided",
    "local": "sam local start-api"
  },
  "dependencies": {
    "@aws-sdk/client-dynamodb": "^3.500.0",
    "@aws-sdk/lib-dynamodb": "^3.500.0",
    "@aws-sdk/client-ses": "^3.500.0",
    "uuid": "^9.0.0"
  },
  "devDependencies": {
    "jest": "^29.7.0",
    "@types/aws-lambda": "^8.10.130"
  }
}`),

  F('f-root-artifact', 'proj-1', 'mule-artifact.json', '/mule-artifact.json', 'json', 'completed',
    `{
  "name": "order-processing",
  "minMuleVersion": "4.4.0",
  "classLoaderModelLoaderDescriptor": {
    "id": "mule",
    "attributes": {
      "exportedResources": ["api/*", "dwl/*"]
    }
  },
  "requiredProduct": "MULE_EE",
  "secureProperties": ["db.password"]
}`,
    `AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: Order Processing API — Migrated from MuleSoft 4

Globals:
  Function:
    Timeout: 30
    Runtime: nodejs18.x
    Environment:
      Variables:
        ORDERS_TABLE: !Ref OrdersTable
        STAGE: !Ref Stage

Parameters:
  Stage:
    Type: String
    Default: dev

Resources:
  OrderFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/order-handler.handler
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref OrdersTable
      Events:
        GetOrders:
          Type: Api
          Properties:
            Path: /api/orders
            Method: get
        CreateOrder:
          Type: Api
          Properties:
            Path: /api/orders
            Method: post
        GetOrderById:
          Type: Api
          Properties:
            Path: /api/orders/{orderId}
            Method: get

  InventoryFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/inventory-handler.handler

  NotificationFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/notification-handler.handler
      Policies:
        - SESCrudPolicy:
            IdentityName: '*'

  OrdersTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub orders-\${Stage}
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      BillingMode: PAY_PER_REQUEST

Outputs:
  ApiUrl:
    Value: !Sub https://\${ServerlessRestApi}.execute-api.\${AWS::Region}.amazonaws.com/Prod/`),

  F('f-root-readme', 'proj-1', 'README.md', '/README.md', 'plaintext', 'completed',
    `# Order Processing MuleSoft Application

## Overview
This MuleSoft 4 application handles order processing for the Acme Corporation e-commerce platform.

## Flows
- **processOrderFlow** — CRUD operations for orders
- **checkInventoryFlow** — Inventory availability checks
- **sendOrderConfirmationFlow** — Email notifications

## Configuration
Edit \`resources/config.properties\` for environment-specific settings.

## Running
\`\`\`bash
mvn clean package -DskipTests
mule deploy -Dmule.env=dev
\`\`\``,
    `# Order Processing — AWS Lambda

## Overview
Migrated from MuleSoft 4 to AWS Lambda + API Gateway + DynamoDB.

## Architecture
| MuleSoft Component | AWS Equivalent |
|---|---|
| HTTP Listener | API Gateway |
| Mule Flows | Lambda Functions |
| Database Connector | DynamoDB |
| Email Connector | Amazon SES |
| DataWeave | JavaScript transforms |
| MUnit Tests | Jest |

## Lambda Functions
- **OrderFunction** — GET/POST /api/orders, GET /api/orders/{orderId}
- **InventoryFunction** — GET /api/inventory/{productId}
- **NotificationFunction** — Sends order confirmation emails via SES

## Deploy
\`\`\`bash
npm install
sam build
sam deploy --guided
\`\`\`

## Local Development
\`\`\`bash
sam local start-api
\`\`\`

## Environment Variables
See \`.env.template\` for required configuration values.`),
];

/* ─────────────────────────────────────────────────────────────────
   Seed demo Migration History — two historical batch runs on proj-1
   so the /history page renders meaningful content out of the box.
   ───────────────────────────────────────────────────────────────── */
const BATCH_1 = 'mig-batch-1740218100-a1b2'; // Feb 22 10:15 — 
const BATCH_2 = 'mig-batch-1740222795-c3d4'; // Feb 22 11:33 — Claude

const _applySeedBatch = (fileIds: string[], batchId: string, provider: LLMProviderType, model: string, createdAt: string) => {
  fileIds.forEach(id => {
    const file = mockFiles.find(f => f.id === id);
    const content = _migratedContentStore[id];
    if (!file || !content) return;
    file.status = 'completed';
    file.migratedContent = content;
    file.activeMigrationId = batchId;
    file.migrations = [
      ...(file.migrations || []),
      { id: batchId, provider, model, content, createdAt, tokens: 0 },
    ];
  });
};

_applySeedBatch(
  ['f-order-flow', 'f-inventory-flow', 'f-notification-flow', 'f-global-config'],
  BATCH_1, 'claude', 'claude-3-7-sonnet-20250219', '2026-02-22T10:15:32Z',
);
_applySeedBatch(
  ['f-transform-order', 'f-config-props', 'f-log4j', 'f-root-pom', 'f-root-artifact', 'f-root-readme'],
  BATCH_2, 'claude', 'claude-3-7-sonnet-20250219', '2026-02-22T11:33:15Z',
);

// Mark error-handler as failed (no migration record — it failed)
const _errFile = mockFiles.find(f => f.id === 'f-error-handler');
if (_errFile) _errFile.status = 'failed';

/* ─── Migration Logs ─── */
export const mockMigrationLogs: MigrationLog[] = [
  { id: 'log-01', projectId: 'proj-1', fileName: 'order-process-flow.xml', timestamp: '2026-02-22T10:15:00Z', status: 'info', message: 'Starting migration of order-process-flow.xml', duration: 0 },
  { id: 'log-02', projectId: 'proj-1', fileName: 'order-process-flow.xml', timestamp: '2026-02-22T10:15:01Z', status: 'info', message: 'Detected 3 flows: getOrdersFlow, createOrderFlow, getOrderByIdFlow', duration: 100 },
  { id: 'log-03', projectId: 'proj-1', fileName: 'order-process-flow.xml', timestamp: '2026-02-22T10:15:02Z', status: 'success', message: 'Successfully migrated 3 MuleSoft flows → single Lambda handler with route switching', duration: 1200 },
  { id: 'log-04', projectId: 'proj-1', fileName: 'inventory-check-flow.xml', timestamp: '2026-02-22T10:15:05Z', status: 'success', message: 'Migrated HTTP request connector → Node.js https module', duration: 800 },
  { id: 'log-05', projectId: 'proj-1', fileName: 'notification-flow.xml', timestamp: '2026-02-22T10:15:08Z', status: 'success', message: 'Email connector → Amazon SES SDK integration', duration: 950 },
  {
    id: 'log-06', projectId: 'proj-1', fileName: 'global-error-handler.xml', timestamp: '2026-02-22T10:15:10Z', status: 'error', message: 'Failed: Unsupported error type mappings (HTTP:UNAUTHORIZED, DB:CONNECTIVITY)', duration: 500, stackTrace: `Error: Unsupported MuleSoft error type mapping
  at MigrationEngine.mapErrorTypes (engine.js:234)
  at MigrationEngine.processErrorHandler (engine.js:189)
  at async MigrationRunner.run (runner.js:89)

Caused by: No direct Lambda equivalent for:
  - HTTP:UNAUTHORIZED → Requires API Gateway Authorizer
  - DB:CONNECTIVITY  → Requires DynamoDB-specific retry logic

Recommendation: Manually implement error middleware using the partial migration output.` },
  { id: 'log-07', projectId: 'proj-1', fileName: 'global-config.xml', timestamp: '2026-02-22T10:15:12Z', status: 'success', message: 'Configuration properties → module.exports / environment variables', duration: 300 },
  { id: 'log-08', projectId: 'proj-1', fileName: 'transform-order.dwl', timestamp: '2026-02-22T10:15:15Z', status: 'success', message: 'DataWeave transform → JavaScript function with equivalent formatting', duration: 1100 },
  { id: 'log-09', projectId: 'proj-1', fileName: 'api-response.dwl', timestamp: '2026-02-22T10:15:18Z', status: 'warning', message: 'RAML DataWeave partially converted — uuid() function replaced with uuid npm package', duration: 600 },
  { id: 'log-10', projectId: 'proj-1', fileName: 'orders-api.raml', timestamp: '2026-02-22T10:15:20Z', status: 'warning', message: 'RAML → OpenAPI 3.0 conversion complete. API Gateway x-amazon integrations added. Manual review recommended for enum types.', duration: 1400 },
  { id: 'log-11', projectId: 'proj-1', fileName: 'config.properties', timestamp: '2026-02-22T10:15:22Z', status: 'success', message: 'Properties file → .env template with AWS-specific variables', duration: 200 },
  { id: 'log-12', projectId: 'proj-1', fileName: 'log4j2.xml', timestamp: '2026-02-22T10:15:24Z', status: 'success', message: 'Log4j configuration → CloudWatch-compatible console logger module', duration: 400 },
  { id: 'log-13', projectId: 'proj-1', fileName: 'pom.xml', timestamp: '2026-02-22T10:15:26Z', status: 'success', message: 'Maven POM → package.json with AWS SDK v3 dependencies', duration: 350 },
  { id: 'log-14', projectId: 'proj-1', fileName: 'mule-artifact.json', timestamp: '2026-02-22T10:15:28Z', status: 'success', message: 'Mule artifact descriptor → SAM template.yaml with API Gateway + DynamoDB resources', duration: 1800 },
  { id: 'log-15', projectId: 'proj-1', fileName: 'README.md', timestamp: '2026-02-22T10:15:30Z', status: 'success', message: 'Documentation updated with AWS deployment instructions and architecture mapping table', duration: 500 },
];

// Export the expected migrated content map for the migration engine
export const expectedMigratedContent: Record<string, string> = { ..._migratedContentStore };

/* ─── Seed Migration Batches — project-level batch records ─── */
export const mockMigrationBatches: MigrationBatch[] = [
  {
    id: BATCH_1,
    projectId: 'proj-1',
    provider: 'claude',
    model: 'claude-3-7-sonnet-20250219',
    status: 'completed',
    startedAt: '2026-02-22T10:14:58Z',
    completedAt: '2026-02-22T10:15:32Z',
    triggeredBy: { userId: 'user-1', userName: 'Harsh Patel' },
    fileResults: [
      { fileId: 'f-order-flow',        fileName: 'order-process-flow.xml',      filePath: '/src/main/mule/order-process-flow.xml',      status: 'completed' },
      { fileId: 'f-inventory-flow',    fileName: 'inventory-check-flow.xml',    filePath: '/src/main/mule/inventory-check-flow.xml',    status: 'completed' },
      { fileId: 'f-notification-flow', fileName: 'notification-flow.xml',       filePath: '/src/main/mule/notification-flow.xml',       status: 'completed' },
      { fileId: 'f-global-config',     fileName: 'global-config.xml',           filePath: '/src/main/mule/global-config.xml',           status: 'completed' },
    ],
    totalFiles: 4,
    completedFiles: 4,
    failedFiles: 0,
    totalTokens: 0,
  },
  {
    id: BATCH_2,
    projectId: 'proj-1',
    provider: 'claude',
    model: 'claude-3-7-sonnet-20250219',
    status: 'partial',
    startedAt: '2026-02-22T11:33:00Z',
    completedAt: '2026-02-22T11:33:15Z',
    triggeredBy: { userId: 'user-1', userName: 'Harsh Patel' },
    fileResults: [
      { fileId: 'f-transform-order',  fileName: 'transform-order.dwl',  filePath: '/src/main/dwl/transform-order.dwl',  status: 'completed' },
      { fileId: 'f-config-props',     fileName: 'config.properties',      filePath: '/resources/config.properties',        status: 'completed' },
      { fileId: 'f-log4j',            fileName: 'log4j2.xml',             filePath: '/resources/log4j2.xml',               status: 'completed' },
      { fileId: 'f-root-pom',         fileName: 'pom.xml',                filePath: '/pom.xml',                            status: 'completed' },
      { fileId: 'f-root-artifact',    fileName: 'mule-artifact.json',     filePath: '/mule-artifact.json',                 status: 'completed' },
      { fileId: 'f-root-readme',      fileName: 'README.md',              filePath: '/README.md',                          status: 'completed' },
      { fileId: 'f-error-handler',    fileName: 'global-error-handler.xml', filePath: '/src/main/mule/global-error-handler.xml', status: 'failed' },
    ],
    totalFiles: 7,
    completedFiles: 6,
    failedFiles: 1,
    totalTokens: 0,
  },
];
